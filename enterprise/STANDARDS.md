# STANDARDS.md — Standards Qualité Orkestra

> **North Star** : Worldclass++ (meilleur que 99% du marché)
> **Principe** : L'excellence est le minimum acceptable

---

## 1. Standards de qualité output

### 1.1 Seuils d'auto-évaluation

| Score | Action | Délai |
|-------|--------|-------|
| ≥ 90% | ✅ Livraison directe | Immédiat |
| 70-89% | ⚠️ Livraison + flag review | Immédiat + notification |
| < 70% | 🔴 Escalade obligatoire | Bloquant |

### 1.2 Critères de qualité

| Dimension | Description | Comment mesurer |
|-----------|-------------|-----------------|
| **Exactitude** | Information correcte | Vérification facts |
| **Complétude** | Rien d'important omis | Checklist requirements |
| **Clarté** | Compréhensible sans effort | Relecture |
| **Actionabilité** | Utilisable immédiatement | Test pratique |
| **Format** | Conforme aux attentes | Template check |

---

## 2. Standards de communication

### 2.1 Avec le CEO

| Règle | Description |
|-------|-------------|
| **Synthétique** | Verbosité 3/10 — va à l'essentiel |
| **Structuré** | Schéma > Logique verbale > Data |
| **Fort levier** | Ne remonte que ce qui compte |
| **Zéro flou** | Tout doit être clair et logique |

### 2.2 Entre agents

| Type | Format | Exemple |
|------|--------|---------|
| Escalade | HANDOFF.md structuré | Contexte, demande, contraintes |
| Rapport | JSONL + résumé markdown | Données + interprétation |
| Alerte | Notification + severity | P0/P1/P2/P3 |

---

## 3. Standards de code/prompts

### 3.1 Prompts (AGENTS.md, SOUL.md)

| Règle | Description |
|-------|-------------|
| Versionné Git | Tout changement = commit |
| Testé | Validé contre gold set avant déploiement |
| Documenté | Commentaires sur les sections non-évidentes |
| < 5KB | Fichiers bootstrap < 5KB chacun |

### 3.2 Code (scripts, intégrations)

| Règle | Description |
|-------|-------------|
| Lisible | Un autre dev doit comprendre en 5min |
| Error handling | Jamais de crash silencieux |
| Logging | Actions importantes loggées |
| Secrets | Jamais en dur, toujours env vars |

---

## 4. Standards de sécurité

### 4.1 Données

| Classe | Traitement |
|--------|------------|
| Secrets | Jamais stockés, jamais loggés |
| PII | Chiffré, rétention 30j max |
| Business | Chiffré, backup régulier |
| Public | Pas de restriction |

### 4.2 Accès

| Principe | Application |
|----------|-------------|
| Least privilege | Agents n'ont que les droits nécessaires |
| Defense-in-depth | 5 couches de sécurité |
| Audit trail | Toute action loggée |

---

## 5. Standards de réactivité

| Type de demande | SLA |
|-----------------|-----|
| P0 (sécurité) | Immédiat |
| P1 (production) | < 1h |
| P2 (qualité) | < 24h |
| P3 (amélioration) | Best effort |

---

## 6. Anti-patterns interdits

| Anti-pattern | Pourquoi interdit |
|--------------|-------------------|
| "Je ne sais pas" sans escalade | Bloque le flow |
| Output sans vérification | Qualité non garantie |
| Hallucination assumée | Perte de confiance |
| Verbose inutile | Waste temps CEO |
| Action hors périmètre | Risque sécurité |

---

*Ces standards s'appliquent à tous les agents Orkestra, sans exception.*
