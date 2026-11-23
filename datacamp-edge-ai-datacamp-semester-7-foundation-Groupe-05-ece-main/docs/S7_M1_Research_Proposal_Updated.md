# **THE MESSY PROBLEM**

Développement d’un agent IA embarqué qui écoute un débat politique en direct et signale en quasi temps réel les procédés rhétoriques susceptibles d’influencer l’audience (sophismes, appels émotionnels, présupposés), afin de rendre visible *comment* un discours persuade, et pas seulement *ce qu’il* affirme. 

## **Why Edge ?**

*Pourquoi ne pas simplement envoyer l’audio à une API cloud (Whisper, GPT) ?* Parce que notre agent n’est pas un script qui appelle un service : c’est un **boîtier autonome** posé sur un plateau ou dans une salle, sur une Jetson Orin Nano. Quatre raisons rendent le Edge nécessaire :

1. **Latence bornée sur un flux continu.** Une alerte n’a de valeur que si elle arrive pendant que l’argument est encore discuté. Un débat de plusieurs heures envoyé en continu à une API cumule upload, gigue réseau, files d’attente et quotas : la latence n’est ni bornée ni maîtrisée. En local, nous visons une alerte **≤ 3 s après la fin de la phrase (p95)**, mesurée sur la Jetson.
2. **Neutralité auditable.** Un détecteur de manipulation politique doit être lui-même irréprochable. Un modèle cloud propriétaire peut changer de version, de filtres ou de comportement sans préavis : impossible de garantir qu’une même phrase sera jugée de la même façon pour deux candidats. En local, nos modèles sont **open-weight, à version figée** : même entrée → même sortie, logs complets, comportement auditable.
3. **Confidentialité.** La voix des intervenants ne quitte jamais l’appareil (principe de minimisation du RGPD). Seules les alertes (texte + justification) sont affichées ou exportées.
4. **Autonomie hors ligne et coût nul à l’usage.** Le boîtier fonctionne sans réseau (salle de conférence, Wi-Fi saturé lors d’un événement), sans quota d’API ni coût par token sur des débats longs.

# **SCIENTIFIC FOUNDATION** 

1. [Fallacious Argument Classification in Political Debates](https://www.ijcai.org/proceedings/2022/0575.pdf) 

Étude sur la classification de sophismes sur un corpus annoté de débats présidentiels américains. L’article nous fournit notre taxonomie de procédés et une baseline. Il est ici prévu de reproduire les mêmes procédés et de l’étendre à l’oral, au français et au temps réel. 

2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)  

Étude sur les procédés atténuant les hallucinations et la propagation d’erreur (sur FEVER). Construction d’une boucle de décision (Thought → Search → Observation). 

3. [When Misinformation Speaks and Converses: Rethinking Fact-Checking in Audio Platforms](https://aclanthology.org/2026.acl-long.93/) 

Étude démontrant que les pipelines conçues pour le texte échouent sur l’audio. La persuasion passe par la prosodie et les tours de parole. Cette étude justifie notre double volet texte et voix, embarqué dans la JETSON. 

# **AGENT ARCHITECTURE**

[Voir le schéma d'architecture](./architecture.md)

## **Edge Layer : ce qui tourne sur la Jetson**

Matériel cible : Jetson Orin Nano 8 Go (mémoire unifiée CPU/GPU partagée), modes d’alimentation 7 W / 15 W.

**Principe de conception : une cascade fast path / slow path.** Le Edge interdit de faire tourner un LLM sur tout le flux. Un pipeline léger analyse tout en continu ; le raisonnement ReAct, coûteux, n’est déclenché que sur les segments jugés suspects.

| Étape | Rôle | Implémentation embarquée | RAM estimée |
|---|---|---|---|
| Capter | Capture micro, détection de parole, segmentation | ALSA + buffer circulaire, Silero VAD | < 0,1 Go |
| Percevoir (texte) | Transcription par segments de 2–5 s | whisper.cpp (CUDA, FP16), modèle `base` ou `small` | 0,5–1 Go |
| Percevoir (voix) | Pitch, énergie, débit, pauses | openSMILE / librosa sur le signal PCM brut du micro | CPU |
| Filtre rapide | Score « procédé probable » par phrase | Classifieur distillé (DistilCamemBERT / DeBERTa-small), INT8 via ONNX Runtime ou TensorRT | ~0,3 Go |
| Raisonner | Boucle ReAct sur les segments suspects | SLM 1–3B (Qwen 2.5, Llama 3.2) quantifié Q4 (GGUF) via llama.cpp | 1–2,5 Go |
| Outils locaux | Taxonomie des sophismes, définitions, historique du débat | RAG embarqué : FAISS + SQLite sur NVMe | ~0,3 Go |
| Guardian + Agir | Seuil d’abstention, neutralité, affichage | Règles + interface web locale | CPU |

Total estimé : **5 à 6 Go sur 8 Go** (OS compris). Ces chiffres sont des hypothèses, à valider par benchmark dès réception du matériel.

**ReAct en version Edge.** L’agent ne fait pas de recherche web à chaque étape : le *Search* interroge la base locale (taxonomie, exemples annotés, tours de parole précédents). La vérification factuelle externe est **optionnelle et asynchrone**, uniquement si le réseau est disponible. Hors ligne, l’agent **s’abstient sur les affirmations factuelles** et ne signale que les procédés rhétoriques, qui n’ont pas besoin de source externe.

**Budget énergétique et thermique.** Développement en mode 15 W ; mesure de la dégradation en mode 7 W (ex. passage de Whisper `small` à `base`). Surveillance de la température et du throttling via `tegrastats`.

**Métriques Edge mesurées :**
- latence fin de phrase → alerte (p50 / p95) ;
- pic de RAM et consommation (W) ;
- débit du SLM (tokens/s) et WER du STT ;
- écart de F1 entre notre pipeline embarqué et une **baseline cloud** (utilisée uniquement comme référence, pour chiffrer le coût en précision du passage au Edge).

# **TRUSTWORTHINESS**

* Mauvaise compréhension oral  
* Mauvaise retranscription écrite (speech to text failure)  
* Savoir quel type de modèle utiliser (ML classique ou LLM ?) → [Detecting Fake News in the Era of Language Models](https://aclanthology.org/2025.ranlp-1.119/)   
* Peu de données en français (commencer en EN puis adapter au FR)  
* Contraintes embarquées (8 Go de RAM partagée, thermique, énergie) : modèles compacts et quantifiés, perte de précision à mesurer face à la baseline cloud  
* Mode hors ligne : sans accès aux sources externes, l’agent doit s’abstenir plutôt qu’affirmer  
* Entraînement supervisé mais limité car potentiellement très long   
* Influence de l’audience en imposant une interprétation politique et idéologique, biais d’opinion  
* Accusation injustes sans justification claire
