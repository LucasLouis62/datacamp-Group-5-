# Architecture Diagrams

Use this file to document your agent architecture with [Mermaid.js](https://mermaid.js.org/) diagrams (ReAct loops, trust filters, simulation interfaces, etc.).

## Agent architecture

Tout ce qui se trouve dans le cadre « Jetson Orin Nano » s’exécute en local. Seule la vérification factuelle web (optionnelle, asynchrone) sort du boîtier.

```mermaid
flowchart LR
    A("<b>Débat TV</b><br>Flux audio live")

    subgraph EDGE ["Jetson Orin Nano · exécution 100 % locale (Edge)"]
        direction LR
        B("<b>Capter</b><br>Micro + VAD<br>buffer circulaire")
        P("<b>Percevoir</b><br>STT whisper.cpp<br>+ prosodie locale")
        R("<b>Filtre rapide</b><br>classifieur INT8<br>fast path, en continu")
        C("<b>Raisonner</b><br>ReAct · SLM 3B Q4<br>si segment suspect")
        E("<b>Outils locaux</b><br>RAG sophismes<br>+ historique débat")
        F("<b>Guardian</b><br>Neutralité, abstention<br>sous seuil, sources")
        D("<b>Agir</b><br>Alerte expliquée<br>écran local")

        B --> P --> R -- "segment suspect" --> C
        C <--> E
        C --> F --> D
    end

    G("<b>Fact-check web</b><br>optionnel, asynchrone")

    A --> B
    E -.-> G

    style EDGE fill:#fafdfb,stroke:#2b7b67,stroke-width:1.5px,stroke-dasharray:6 4,color:#0b4d3e

    classDef greyBox fill:#f2eee9,stroke:#6e6962,stroke-width:1.5px,color:#262626
    classDef greenBox fill:#e2f4ed,stroke:#2b7b67,stroke-width:1.5px,color:#0b4d3e
    classDef redBox fill:#faebe5,stroke:#9e4b35,stroke-width:1.5px,color:#7a2b18
    classDef extBox fill:#ffffff,stroke:#6e6962,stroke-width:1.5px,stroke-dasharray:4 3,color:#262626

    class A,E greyBox
    class B,P,R,C,D greenBox
    class F redBox
    class G extBox

    linkStyle default stroke:#6e6962,stroke-width:1.5px
```

## Edge pipeline (fast path / slow path)

```mermaid
sequenceDiagram
    participant Mic as Micro (ALSA)
    participant STT as STT + prosodie
    participant Clf as Filtre rapide (INT8)
    participant Agent as ReAct (SLM Q4)
    participant RAG as RAG local
    participant UI as Guardian + écran

    loop Toutes les 2–5 s (fast path)
        Mic->>STT: segment audio PCM
        STT->>Clf: texte + features prosodiques
    end
    alt score > seuil (slow path)
        Clf->>Agent: segment suspect + contexte
        Agent->>RAG: Search (taxonomie, historique)
        RAG-->>Agent: Observation
        Agent->>UI: procédé + justification + confiance
        UI-->>UI: abstention si confiance < seuil
    end
```
