---
config:
  theme: base
  layout: fixed
---

---

config:
theme: base
layout: fixed

---

flowchart TB
subgraph CORE["**Core AI Orchestration**"]
direction TB
Agent["<b>AgentModule</b><br>Agent loop and orchestration"]
Llm["<b>LlmModule</b><br>LLM providers and model access"]
Tools["<b>ToolsModule</b><br>MCP tools integration"]
end
subgraph DOMAIN["**Business Domain Modules**"]
direction TB
Projects["<b>ProjectsModule</b><br>Project logic"]
Stories["<b>UserStoriesModule</b><br>User stories management"]
Tests["<b>TestsModule</b><br>Test execution"]
end
subgraph INFRA["**Infrastructure and Persistence**"]
direction TB
Cache["<b>StorageModule</b><br>Cache and data storage"]
Files["<b>FileStorageModule</b><br>Generated file handling"]
Config["<b>ConfigModule</b><br>Configuration &amp; environment"]
end
App["<b>AppModule</b><br>Root module"] --> CORE & DOMAIN & INFRA
CORE --> INFRA
DOMAIN --> INFRA
CORE --> DOMAIN

     Agent:::core
     Llm:::core
     Tools:::core
     Projects:::domain
     Stories:::domain
     Tests:::domain
     Cache:::infra
     Files:::infra
     Config:::infra
     App:::root
    classDef root fill:transparent,stroke:#111827,color:#111827,stroke-width:2px
    classDef core fill:#e6f0ff,stroke:#1d4ed8,color:#1e3a8a,stroke-width:1.5px
    classDef domain fill:#eaf7ee,stroke:#15803d,color:#14532d,stroke-width:1.5px
    classDef infra fill:#fff4e8,stroke:#c2410c,color:#7c2d12,stroke-width:1.5px
    style CORE fill:#f0f6ff,stroke:#1d4ed8,stroke-width:2.5px,color:#1d4ed8,font-weight:bold
    style DOMAIN fill:#f4fbf6,stroke:#15803d,stroke-width:2.5px,color:#15803d,font-weight:bold
    style INFRA fill:#fff8f3,stroke:#c2410c,stroke-width:2.5px,color:#c2410c,font-weight:bold
