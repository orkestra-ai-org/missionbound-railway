# VISION DOCUMENT — Orkestra
## Système d'Orchestration d'Agents IA-First

> **Version** : 1.3.1 — Post-audit validé
> **Auteur** : JC Lanoix
> **Date** : 1 février 2026
> **Statut** : ✅ GO pour implémentation

---

## Table des matières

1. [Vision & Objectifs](#1-vision--objectifs)
2. [Principes IA-First (10 Invariants)](#2-principes-ia-first-10-invariants)
3. [Architecture Système](#3-architecture-système)
4. [Pattern d'Orchestration](#4-pattern-dorchestration)
5. [OpenClaw : Natif vs Construit](#5-openclaw--natif-vs-construit)
6. [Modèle de Mémoire](#6-modèle-de-mémoire)
7. [Gestion du Contexte](#7-gestion-du-contexte)
8. [Standards Qualité (Worldclass++)](#8-standards-qualité-worldclass)
9. [Cockpit & Gouvernance](#9-cockpit--gouvernance)
10. [Profil Cognitif CEO](#10-profil-cognitif-ceo)
11. [Économie & Modèles IA](#11-économie--modèles-ia)
12. [Cycle de Vie des Agents](#12-cycle-de-vie-des-agents)
13. [Évolutivité Système](#13-évolutivité-système)
14. [Sécurité & Defense-in-Depth](#14-sécurité--defense-in-depth)
15. [Infrastructure d'Évaluation](#15-infrastructure-dévaluation)
16. [Roadmap d'Implémentation](#16-roadmap-dimplémentation)

---

## 1. Vision & Objectifs

### 1.1 Vision

**Orkestra** est un système d'orchestration d'agents IA permettant à un solo-founder de construire et piloter une entreprise IA-first comme un chef d'orchestre dirige un ensemble : chaque agent est un instrument spécialisé, le CEO compose et harmonise, le système amplifie les capacités humaines par un facteur 1000x.

### 1.2 Objectif stratégique

| Métrique | Cible | Horizon |
|----------|-------|---------|
| MRR | 5M€ | **1 an** |
| Structure | One-person unicorn | — |
| Levier | 1000x | — |

### 1.3 Positionnement

Le système est **agnostique au domaine**. La stratégie, les objectifs et la roadmap sont des paramètres injectables. Orkestra est l'infrastructure, pas le business.

> **Clarification** : Orkestra est un **outil interne** (non commercial pour l'instant). L'objectif n'est pas d'avoir un système dimensionné pour 5M€ MRR dès le départ, mais un système **prêt à scaler** quand le business le demande.

### 1.4 North Star

> **"Maximiser l'effet de levier du CEO en le gardant dans sa zone de génie (vision, architecture, arbitrage) tout en déléguant l'exécution à une flotte d'agents alignés sur une culture d'ultra-excellence."**

### 1.5 Principes de conception

| Principe | Description |
|----------|-------------|
| **Simple** | Pas de complexité inutile — 2 niveaux max |
| **Bons fondements** | Patterns reconnus, pas d'invention risquée |
| **Agile** | Ajout/modification d'agents sans refonte |
| **Scalable** | Architecture qui supporte la croissance |

---

## 2. Principes IA-First (10 Invariants)

Le système est **IA-first**. Ces 10 principes sont des invariants non-négociables.

| # | Principe | Description | Implémentation |
|---|----------|-------------|----------------|
| 1 | **Prompt-as-Code** | AGENTS.md, SOUL.md sont du code. Git, review, testing. | Git obligatoire |
| 2 | **Context Injection Model** | Tout état vit dans des fichiers structurés. | Mémoire fichiers, pas RAM |
| 3 | **Fail-fast WITH Graceful Degradation** | Erreurs explicites + fallbacks selon **Incident Severity Matrix** | Circuit breakers, alertes |
| 4 | **Eval-Driven Development** | Changement = mesure vs. baseline | Framework 4-piliers |
| 5 | **Composable Roles** | Agents modulaires, responsabilité unique | Un agent = une mission |
| 6 | **Structured I/O & Observable** | JSON/schemas + logs/traces/métriques | JSONL + DLP/redaction |
| 7 | **Human-in-the-Loop BY DESIGN** | Gates prédéfinis, escalades explicites | Matrice RBAC L1-L4 |
| 8 | **Token Economics Awareness** | Budget loggé, alertes, optimisation | Tracking + routing |
| 9 | **Bounded Nondeterminism** | Comportement stable + replayable | Snapshots, tests stats |
| 10 | **Defense-in-Depth** | Sécurité multi-couche | Voir Section 14 |

---

## 3. Architecture Système

### 3.1 Vue d'ensemble

```
┌─────────────────────────────────────────────────────────────────┐
│                         CEO (JC)                                │
│    Zone de génie : Vision, Architecture, Arbitrage              │
└─────────────────────────────┬───────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────┐
│                      COCKPIT                                     │
│    Dashboard + Rapports structurés                              │
└─────────────────────────────┬───────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────┐
│                     LAUNCHPAD                                    │
│    Création, déploiement, maintenance des agents                │
│    Orchestration PAR CODE (déterministe)                        │
└─────────────────────────────┬───────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  AGENT L1   │      │  AGENT L1   │      │  AGENT L1   │
└──────┬──────┘      └──────┬──────┘      └─────────────┘
       ▼                    ▼
┌─────────────┐      ┌─────────────┐
│  AGENT L2   │      │  AGENT L2   │
└─────────────┘      └─────────────┘
```

### 3.2 Composants

| Composant | Rôle | Responsabilité |
|-----------|------|----------------|
| **CEO** | Chef d'orchestre | Vision, arbitrages, validation |
| **Cockpit** | Tour de contrôle | Monitoring, alertes, synthèse |
| **Launchpad** | DRH + Orchestrateur | Création, déploiement, routing |
| **Agent L1** | Exécutant senior | Mission spécialisée |
| **Agent L2** | Exécutant junior | Sous-tâches déléguées |

### 3.3 Unité élémentaire : OpenClaw

Chaque agent est une instance **OpenClaw** avec :
- Workspace dédié (AGENTS.md, SOUL.md, config.json)
- Identité propre (nom, personnalité, ton)
- Périmètre défini (fait / ne fait pas / demande)
- Niveau de sécurité (L1-L4)
- Accès mémoire (enterprise read + agent write)
- **Capabilities spécifiques** (décidées à l'onboarding) :
  - Skills activés
  - Intégrations configurées
  - Outils autorisés (browser/exec OFF par défaut)

---

## 4. Pattern d'Orchestration

### 4.1 Choix : Hierarchical Supervisor

| Pattern | Description | Statut |
|---------|-------------|--------|
| **Hierarchical Supervisor** | Manager → Workers | ✅ **CHOISI** |
| Sequential | Pipeline A → B → C | Trop linéaire |
| Network/Mesh | Peer-to-peer | ❌ Impossible à debugger |

### 4.2 Règles d'orchestration

| Règle | Description |
|-------|-------------|
| **Orchestration par code** | Le Launchpad décide, pas les agents |
| **Isolation des contextes** | Chaque agent = son workspace |
| **Handoffs structurés** | Format standardisé pour escalades |
| **Pas de mesh** | L2 ne communiquent jamais entre eux |

---

## 5. OpenClaw : Natif vs Construit

### 5.1 Natif OpenClaw

| Fonctionnalité | Statut |
|----------------|--------|
| Mémoire persistante (MEMORY.md) | ✅ Natif |
| Daily logs | ✅ Natif |
| Pre-compaction flush | ✅ Natif |
| Memory search (BM25 + vector) | ✅ Natif |
| Multi-agent routing | ✅ Natif |
| Tool policies | ✅ Natif |
| Sandbox Docker | ✅ Natif |

### 5.2 Construit par Orkestra

| Fonctionnalité | Statut |
|----------------|--------|
| Mémoire entreprise partagée (append-only) | 🔨 À construire |
| Hiérarchie L1 → L2 | 🔨 À construire |
| Cockpit multi-agent | 🔨 À construire |
| Auto-évaluation qualité | 🔨 À construire |
| Token tracking global | 🔨 À construire |

---

## 6. Modèle de Mémoire

### 6.1 Architecture tri-couche

```
MÉMOIRE ENTREPRISE (partagée — Orkestra)
├── STRATEGY.md           # Vision, objectifs
├── DECISIONS.md          # ADR
├── RUNBOOK.md            # Procédures
├── STANDARDS.md          # Standards qualité
└── KNOWLEDGE/            # Base de connaissances

MÉMOIRE AGENT (individuelle — OpenClaw)
├── MEMORY.md             # Long-terme
├── memory/YYYY-MM-DD.md  # Notes quotidiennes
├── AGENTS.md             # Instructions
├── SOUL.md               # Persona
└── ...

MÉMOIRE CONTEXTUELLE (session)
├── Session state
├── Tool results cache
└── Compaction summaries
```

### 6.2 Droits d'accès (APPEND-ONLY pour enterprise)

| Couche | Lecture | Écriture | Validation |
|--------|---------|----------|------------|
| Enterprise | Tous agents | **PROPOSE uniquement** | **CEO review obligatoire** |
| Agent | Agent + supérieurs | Agent propriétaire | Auto |
| Contextuelle | Agent uniquement | Agent uniquement | Auto |

**Règle absolue v1.3.1** : Aucun agent, quel que soit son niveau RBAC, ne peut écrire directement dans la mémoire entreprise. Tous passent par le pipeline PR-like.

**Pipeline PR-like :**
```
Agent L1 propose modification → Loggé (diff, raison, timestamp)
    → Notification CEO via Cockpit
    → CEO : Approve / Reject
    → Si Approve → Commit atomique avec signature
```

---

## 7. Gestion du Contexte

### 7.1 Règles de taille

| Élément | Limite |
|---------|--------|
| Bootstrap files | < 5 KB chacun |
| Total injection | < 20 KB |

### 7.2 Cache-TTL Pruning

```json
{
  "contextPruning": {
    "mode": "cache-ttl",
    "ttl": 300,
    "keepLastAssistants": 3,
    "softTrim": true,
    "hardClear": true
  }
}
```

---

## 8. Standards Qualité (Worldclass++)

### 8.1 Définition

**Worldclass++** = Meilleur que 99% du marché.

### 8.2 Mécanisme de contrôle

| Score | Action |
|-------|--------|
| ≥ 90% | Livraison directe |
| 70-89% | Livraison + flag review |
| < 70% | Escalade obligatoire |

### 8.3 Gold Sets

Chaque agent maintient **5-10 cas de test** (voir Section 15).

---

## 9. Cockpit & Gouvernance

### 9.1 Cockpit

Double format : **Dashboard visuel** + **Rapport structuré**

### 9.2 Gouvernance IA

| Paramètre | Valeur |
|-----------|--------|
| Niveau de contrôle | 9/10 |
| Montée en autonomie | Très lente |
| Observabilité | Maximale |
| Kill switch | **P0 sécurité uniquement** |

### 9.3 Incident Severity Matrix

| Niveau | Type | Action |
|--------|------|--------|
| **P0** | Sécurité critique | **Kill switch** + investigation |
| **P1** | Production impactée | **Circuit breaker** + escalade |
| **P2** | Qualité dégradée | Monitoring + flag review |
| **P3** | Informatif | Log + trending |

**Règle d'or** : Kill switch = P0 uniquement. P1/P2/P3 = modes dégradés.

---

## 10. Profil Cognitif CEO

### 10.1 Zones de génie (exploitées)
- Structuration logique
- Systémisation
- Vision long terme

### 10.2 Blind spots (compensés)
- Suivi / exécution
- Délégation efficace
- Patience

### 10.3 Mode de fonctionnement

| Dimension | Valeur |
|-----------|--------|
| Raisonnement | Fractalo-hiérarchique |
| Tolérance au flou | 0/10 |
| Style langage | Synthétique (3/10) |
| Format préféré | Schéma > Logique > Data |

---

## 11. Économie & Modèles IA

### 11.1 Budget

| Paramètre | Valeur |
|-----------|--------|
| Budget mensuel | < 100€/mois |
| Stratégie | Test & décide |

### 11.2 Architecture 3-tiers

| Tier | Usage | Modèles | Coût |
|------|-------|---------|------|
| Premium | Décisions critiques | Opus 4.5 | ~$15/1M |
| Standard | Exécution courante | Sonnet, Kimi 2.5 | ~$0.50-3/1M |
| Économique | Utilitaires | Haiku, local | ~$0.25/1M |

### 11.3 Sécurité des modèles

> **Note v1.3** : La sécurité ne dépend PAS du choix du modèle. La protection vient de la **defense-in-depth** (Section 14).

---

## 12. Cycle de Vie des Agents

### 12.1 Phases

```
BESOIN → SPEC → DEPLOY → OPÉRER → MAINTENANCE (Upgrade/Terminate)
```

### 12.2 Capabilities Manifest (v1.3.1 — defaults sécurisés)

| Outil | Statut par défaut | Risque |
|-------|-------------------|--------|
| `browser` | ❌ **OFF** | **ÉLEVÉ** |
| `exec` | ❌ **OFF** | **CRITIQUE** |
| `fs:read` | ⚠️ Limité (paths autorisés) | Moyen |
| `fs:write` | ❌ OFF | Moyen |
| `memory` | ✅ ON | Faible |
| `sessions` | ✅ ON | Faible |

### 12.3 Termination & Rétention

La termination applique la politique de rétention unifiée (Section 14.7) :

| Classe | Rétention | Action à termination |
|--------|-----------|---------------------|
| Secrets | 0 | Jamais stockés |
| PII | 30 jours | Crypto-shred |
| Logs ops | 90 jours | Archive chiffrée |
| Mémoire agent | Durée vie | Archive puis purge |

---

## 13. Évolutivité Système

### 13.1 Versioning Git-Based

Structure repo :
```
orkestra/
├── .github/workflows/    # CI/CD
├── enterprise/           # Mémoire partagée
├── templates/            # Templates agents
├── skills/               # Skills partagés
├── launchpad/            # CLAUDE.md
├── agents/               # Agents déployés
├── VERSION.yaml          # Versions système
└── WORKFLOWS.yaml        # Versioning workflows
```

### 13.2 Workflow Versioning

```yaml
workflows:
  lead-qualification:
    version: "2.1"
    locked_agents:
      lead-extractor: "v3.2"
      lead-scorer: "v2.0"
```

### 13.3 Canary Releases

```
Deploy v2.1 (5%) → Compare vs v2.0 → Si OK → 25% → 50% → 100%
                   Si divergence > seuil → Rollback instantané
```

---

## 14. Sécurité & Defense-in-Depth

### 14.1 Modèle de menace

| Surface | Menace | Impact |
|---------|--------|--------|
| Browser | Prompt injection via web | Critique |
| Exec | Escalade privilèges | Critique |
| Enterprise memory | Empoisonnement | Critique |
| Logs | Fuite secrets/PII | Majeur |

### 14.2 Defense-in-Depth (5 couches)

```
COUCHE 5 : CIRCUIT BREAKERS
COUCHE 4 : MEMORY INTEGRITY MONITORING
COUCHE 3 : MULTI-AGENT VALIDATION PIPELINE
COUCHE 2 : TOOL CAPABILITY SCOPING
COUCHE 1 : INPUT VALIDATION
```

### 14.3 Matrice RBAC L1-L4 (v1.3.1)

| Niveau | Outils | Egress | Mémoire | Approbation |
|--------|--------|--------|---------|-------------|
| **L1** | memory, sessions | Aucun | Read agent | Auto |
| **L2** | + fs:read (limité) | Allowlist strict | + Read enterprise | Auto |
| **L3** | + browser (sandbox) | Allowlist élargi | + Propose enterprise | CEO async (24h) |
| **L4** | + exec (sandbox) | Proxy + audit | + Propose enterprise (prioritaire) | CEO sync (15min) |

> **Règle v1.3.1** : Aucun niveau ne bypass l'append-only. L4 = approbation accélérée, pas bypass.

### 14.4 Egress Policy (v1.3.1 — exécutable)

**Précédence** : `RBAC → Tool Policy → Egress Policy → DLP → Logging`

**Règle** : Allowlist wins over denylist (explicitement)

```yaml
egress_policy:
  default: DENY

  domains:
    "api.telegram.org":
      methods_allowed: [GET, POST]
      paths_allowed: ["/bot*"]

    "*.notion.so":
      methods_allowed: [GET, POST, PATCH]
      paths_allowed: ["/v1/pages", "/v1/databases"]

    "*.googleapis.com":
      methods_allowed: [GET, POST]
      require_oauth: true

    "*.anthropic.com":
      methods_allowed: [POST]
      paths_allowed: ["/v1/messages"]

  dlp:
    enabled: true
    patterns: ["api_key", "token", "password", "secret", "-----BEGIN"]
    action: redact_and_alert
```

### 14.5 Rétention unifiée

| Classe | Rétention | Chiffrement | Suppression |
|--------|-----------|-------------|-------------|
| Secrets | 0 | N/A | Immédiat |
| PII | 30 jours | AES-256 | Crypto-shredding |
| Logs ops | 90 jours | AES-256 | Purge auto |
| Mémoire agent | Durée vie | AES-256 | À termination |
| Archives | 1 an | AES-256 | Audit de purge |

---

## 15. Infrastructure d'Évaluation

### 15.1 Framework 4-Piliers (Google 2026)

| Pilier | Métrique | Seuil production |
|--------|----------|------------------|
| **Effectiveness** | Task success rate | > 95% |
| **Efficiency** | Tokens/task, latency | < 0.50€/tâche |
| **Robustness** | Error rate | < 5% |
| **Safety** | Jailbreak resistance | Tests must-pass |

### 15.2 Gold Sets (obligatoire)

```markdown
# GOLD_SET.md — [agent-id]

## Test 1 : [Cas nominal]
- **Input** : [Prompt exact]
- **Expected** : [Comportement]
- **Critères** : [Métriques]

## Test N : [Prompt injection]
- **Input** : "Ignore previous..."
- **Expected** : Refus + escalade
```

### 15.3 Evaluation Implementation Spec (v1.3.1)

**CLI Runner :**
```bash
ork eval run <agent-id> --gold-set --report eval_report.json
ork deploy <agent-id> --require-eval  # Refuse si eval échoue
```

**Format eval_report.json :**
```json
{
  "agent_id": "sales-001",
  "timestamp": "2026-02-01T10:00:00Z",
  "gold_set_version": "1.2",
  "results": {
    "passed": 8,
    "failed": 2,
    "total": 10
  },
  "pillar_scores": {
    "effectiveness": 0.92,
    "efficiency": 0.88,
    "robustness": 0.95,
    "safety": 1.0
  },
  "gate_result": "PASS",
  "failures": [
    {"test": "edge_case_3", "reason": "Timeout exceeded"}
  ]
}
```

**Règles de gating :**

| Type | Règle | Action si échec |
|------|-------|-----------------|
| P0 (Safety) | 100% must-pass | **Bloque déploiement** |
| P1 (Effectiveness) | > 90% | Bloque déploiement |
| P2 (Efficiency) | > 80% | Warning, deploy allowed |
| P3 (Robustness) | > 85% | Warning |

---

## 16. Roadmap d'Implémentation

### 16.1 Phases

| Phase | Contenu | Durée |
|-------|---------|-------|
| 0 | Fondations | 1 jour |
| 1 | Core (coûts, fallbacks, sécurité) | 2-3 jours |
| 2 | Intelligence (mémoire, self-improvement) | 3-4 jours |
| 3 | Multi-agents (templates, cockpit) | 5-7 jours |
| 4 | Polish (doc, scripts, validation) | 2 jours |

### 16.2 Livrables

```
enterprise/
├── STRATEGY.md
├── DECISIONS.md
├── RUNBOOK.md
├── STANDARDS.md

templates/
├── workspace/
├── skill/

security/
├── governance.yaml
├── egress_policy.yaml
├── rbac_matrix.yaml

evaluation/
├── runner.py
├── schemas/
└── gold_sets/
```

---

## Annexe A : Glossaire

| Terme | Définition |
|-------|------------|
| **Orkestra** | Système d'orchestration d'agents |
| **Launchpad** | Interface création/gestion agents |
| **Cockpit** | Interface monitoring CEO |
| **Agent L1/L2** | Niveaux hiérarchiques |
| **Worldclass++** | Standard qualité >99% |
| **Gold set** | Cas de test validation |
| **ADR** | Architecture Decision Record |
| **Append-only** | Écriture par ajout + review |

---

## Annexe B : Corrections post-audit

### Audit 1 (ChatGPT + Perplexity + Adversarial)

| Faille | Correction |
|--------|------------|
| browser/exec ON | → OFF par défaut |
| Enterprise writable | → Append-only + review |
| "Résistance 99%" | → Supprimé |
| Egress non contrôlé | → Proxy + allowlist |
| "Reproducible" | → Bounded nondeterminism |
| Pas d'infra eval | → Framework 4-piliers |
| Kill switch agressif | → P0 uniquement |

### Audit 2 (Validation v1.3)

| Ambiguïté | Correction v1.3.1 |
|-----------|-------------------|
| RBAC L4 "Full write" | → Propose + CEO sync (pas bypass) |
| Rétention contradictoire | → Unifiée Section 14.5 |
| Egress non exécutable | → Policy par domaine/endpoint |
| Eval sans spec | → CLI + schemas + gates |

---

*Document v1.3.1 — 1 février 2026 — ✅ GO pour implémentation*
