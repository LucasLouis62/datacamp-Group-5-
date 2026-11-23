# Datacamp Project: Trustworthy Edge Agents for a Dynamic World

Welcome to the Datacamp Project. This repository will house your code for the next three semesters. This project challenges your 6-person group to engineer a physically situated, Agentic AI system that performs on severely constrained Edge hardware while maintaining demonstrable trustworthiness.

## 1. Project Lifecycle & Constraints
* **Semester 7 (Sim & Architecture):** Focus on Agent structure and simulated domains. *Constraint: Code-level trustworthiness.*
* **Semester 8 (Physicalization):** Focus on sim-to-real transfer onto Jetson Nano Orin hardware. *Constraint: Edge latency.*
* **Semester 9 (Agentic Product):** Focus on GenAI, local LLMs, and productization. *Constraint: Real-time ethical UX.*

## 2. The Evolutionary Role Matrix
To ensure active coding and balanced workloads, each student adopts a Phase-Based Role. You must distribute these 6 tracks among your group.

| Track | S7: Simulation & Architecture | S8: Physicalization (The Edge) | S9: Agentic Product (GenAI) |
| :--- | :--- | :--- | :--- |
| **1. The Brain (AI/LLM Architect)** | **Simulation Logic:** Codes core ReAct reasoning loops and tests simulated logic. | **Model Optimizer:** Prunes and quantizes models to run efficiently on Jetson Nano. | **GenAI Architect:** Integrates local LLMs and manages prompt chaining. |
| **2. The Body (Edge/Hardware)** | **Sim-Environment:** Builds physics/text simulation and mocks hardware APIs. | **Edge Hardware Lead:** Owns Jetson deployment, sensor integration, and sim-to-real transfer. | **GPU Manager:** Routes heavy GenAI compute loads to shared 96GB GPUs. |
| **3. The Librarian (Data/Backend)** | **Dataset Curator:** Scrapes and structures training data. Builds mock databases. | **State Manager:** Builds fast NOSQL databases on the Edge device for agent memory. | **RAG Engineer:** Builds document-retrieval pipelines and vector databases. |
| **4. The Pipeline (MLOps/QA)** | **Testing Lead:** Sets up GitHub Actions and automated logic tests. | **MLOps & Docker:** Containerizes the agent via Docker; tracks live latency/FPS. | **Reliability Eng:** Manages version control for complex AI models; ensures 99% uptime. |
| **5. The Guardian (Trust/Ethics)** | **Metric Designer:** Translates ethics into programmable code constraints. | **Fail-safe Coder:** Codes physical hard-stops and collision avoidance protocols. | **Algorithmic Auditor:** Red-teams the agent and conducts the final Ethics Audit. |
| **6. The Face (UI/UX & Product)** | **Research Lead:** Writes the academic proposal and manages sprint tracking. | **Hardware API:** Manages lab booking and builds API endpoints for the Edge device. | **UX Lead:** Builds the final front-end interface and leads the Shark Tank pitch. |

## 3. S9 Mergers & Acquisitions (M&A) Protocol
Due to natural cohort attrition (e.g., double-diploma programs) between S8 and S9, an M&A strategy applies. 
* At the end of S8, projects are audited. The strongest become "Host Projects." 
* Surviving students from retired groups become "Free Agents." 
* Free Agents are drafted into Host Projects at the start of S9, bringing a **"Tech-Pivot"**—a successfully coded module from their S8 project to integrate into their new team.

## 4. Sprint Calendars & Deliverables

### Semester 7: Foundations & Simulation
| Month | Expected Deliverable | Reconduction / Threat Mitigation |
| :--- | :--- | :--- |
| **M1** | 1-page Research Proposal (3 SOTA papers cited, ReAct architecture). | **Threat:** Weak scientific basis. **Action:** Rewrite if papers aren't top-tier. |
| **M2** | Functional simulated environment. Dataset description. Automated tests. | **Threat:** Environment is too simple. **Action:** Code sent back for revision. |
| **M3** | Agent operates in sim. First code-level 'Trust Check' implemented. | **Threat:** Agent breaks rules. **Action:** Mandatory Office Hours with Trust Engineer. |
| **M4** | **Poster & Pitch Session.** Scored on clarity, SOTA foundation, code structure. | **Threat:** Poor presentation. **Action:** Score dictates S8 starting privileges. |

### Semester 8: Physicalization & MLOps
| Month | Expected Deliverable | Reconduction / Threat Mitigation |
| :--- | :--- | :--- |
| **M1** | Sim-to-real transfer plan. Latency bottleneck analysis. Booking System integration. | **Threat:** Unrealistic demands. **Action:** Redesign model architecture for Edge limits. |
| **M2** | Agent containerized (Docker). 'Hello World' service deployed to shared Jetson. | **Threat:** Dependency hell. **Action:** Cannot book physical lab time until Docker builds. |
| **M3** | First physical test on Jetson/Robot. Edge latency data gathered. Math tuning applied. | **Threat:** Latency > 1s. **Action:** Group must optimize code live in the "War-Room". |
| **M4** | **Live Tech Demo.** Solve an unknown edge case live in 15 mins. | **Threat:** System crash. **Action:** Immediate M&A evaluation (Host vs. Free Agent). |

### Semester 9: Agentic Product & Excellence
| Month | Expected Deliverable | Reconduction / Threat Mitigation |
| :--- | :--- | :--- |
| **M1** | M&A Integration complete. Refined local LLM deployed to edge or remote GPU queue. | **Threat:** Free Agent tech rejected. **Action:** Faculty mediation to force integration. |
| **M2** | Integration of RAG or custom Recommender System (RecSys) for contextual behavior. | **Threat:** RAG retrieves garbage. **Action:** Dataset must be manually re-curated. |
| **M3** | Ethics Audit passed. Code includes a dedicated, unbreakable ethics filtering layer. | **Threat:** Fails safety test. **Action:** Hard block. Cannot pitch in M4 until resolved. |
| **M4** | **Investor Pitch (Shark Tank).** 10-minute pitch to faculty and industry judges. | Final Grade Assessment. |

## 5. Setup Instructions & Repository Rules
1. **Never commit massive data files:** `.pt`, `.h5`, and large `.csv` files MUST be strictly ignored via `.gitignore`. 
2. **MinIO Integration:** Heavy datasets and model weights must be stored externally and fetched dynamically via API calls in your scripts.
3. **Branch Protection:** All code must be submitted via Pull Requests. Do not push directly to the `main` branch.
