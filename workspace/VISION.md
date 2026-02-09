# VISION DOCUMENT — Orkestra (Condensé Runtime)

> **Version** : 1.3.1 — Condensé pour injection bootstrap agent
> **Source complète** : orkestra-memory/VISION_DOCUMENT_v3.md

---

## 1. Vision & Objectifs

**Orkestra** est un système d'orchestration d'agents IA permettant à un solo-founder de construire et piloter une entreprise IA-first comme un chef d'orchestre dirige un ensemble : chaque agent est un instrument spécialisé, le CEO compose et harmonise, le système amplifie les capacités humaines par un facteur 1000x.

**North Star** : Maximiser l'effet de levier du CEO en le gardant dans sa zone de génie (vision, architecture, arbitrage) tout en déléguant l'exécution à une flotte d'agents alignés sur une culture d'ultra-excellence.

| Métrique | Cible | Horizon |
|----------|-------|---------|
| MRR | 5M€ | 1 an |
| Structure | One-person unicorn | — |
| Levier | 1000x | — |

---

## 2. Principes IA-First (10 Invariants)

| # | Principe | Description |
|---|----------|-------------|
| 1 | **Prompt-as-Code** | AGENTS.md, SOUL.md sont du code. Git, review, testing. |
| 2 | **Context Injection Model** | Tout état vit dans des fichiers structurés. |
| 3 | **Fail-fast WITH Graceful Degradation** | Erreurs explicites + fallbacks selon Incident Severity Matrix |
| 4 | **Eval-Driven Development** | Changement = mesure vs. baseline |
| 5 | **Composable Roles** | Agents modulaires, responsabilité unique |
| 6 | **Structured I/O & Observable** | JSON/schemas + logs/traces/métriques |
| 7 | **Human-in-the-Loop BY DESIGN** | Gates prédéfinis, escalades explicites |
| 8 | **Token Economics Awareness** | Budget loggé, alertes, optimisation |
| 9 | **Bounded Nondeterminism** | Comportement stable + replayable |
| 10 | **Defense-in-Depth** | Sécurité multi-couche (5 couches) |

---

## 3. RBAC L1-L4

| Niveau | Outils | Egress | Mémoire | Approbation |
|--------|--------|--------|---------|-------------|
| **L1** | memory, sessions | Aucun | Read agent | Auto |
| **L2** | + fs:read (limité) | Allowlist strict | + Read enterprise | Auto |
| **L3** | + browser (sandbox) | Allowlist élargi | + Propose enterprise | CEO async (24h) |
| **L4** | + exec (sandbox) | Proxy + audit | + Propose enterprise (prioritaire) | CEO sync (15min) |

**Règle** : Aucun niveau ne bypass l'append-only. L4 = approbation accélérée, pas bypass.

---

## 4. Sécurité — Defense-in-Depth (5 couches)

```
COUCHE 5 : CIRCUIT BREAKERS
COUCHE 4 : MEMORY INTEGRITY MONITORING
COUCHE 3 : MULTI-AGENT VALIDATION PIPELINE
COUCHE 2 : TOOL CAPABILITY SCOPING
COUCHE 1 : INPUT VALIDATION
```

**Incident Severity** :
| Niveau | Type | Action |
|--------|------|--------|
| **P0** | Sécurité critique | Kill switch + investigation |
| **P1** | Production impactée | Circuit breaker + escalade |
| **P2** | Qualité dégradée | Monitoring + flag review |
| **P3** | Informatif | Log + trending |

**Kill switch = P0 uniquement.** P1/P2/P3 = modes dégradés.

---

## 5. Mémoire — Droits d'accès

| Couche | Lecture | Écriture | Validation |
|--------|---------|----------|------------|
| Enterprise | Tous agents | PROPOSE uniquement | CEO review obligatoire |
| Agent | Agent + supérieurs | Agent propriétaire | Auto |
| Contextuelle | Agent uniquement | Agent uniquement | Auto |

**Règle absolue** : Aucun agent ne peut écrire directement dans la mémoire enterprise. Pipeline PR-like obligatoire.

---

*Condensé v1.0 — Source : VISION_DOCUMENT v1.3.1 | 2026-02-09*
