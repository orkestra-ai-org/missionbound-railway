# TOOLS.md — Configuration des outils Orkestra

> Notes sur les outils disponibles et leurs conventions

---

## Outils natifs OpenClaw

### Memory
- **Statut** : ✅ Activé
- **Usage** : Mémoire persistante via MEMORY.md et memory/
- **Convention** : Flush avant compaction, read au démarrage

### Sessions
- **Statut** : ✅ Activé
- **Usage** : Gestion des conversations
- **Convention** : Une session = un contexte isolé

### File System (Read)
- **Statut** : ⚠️ Limité
- **Scope** : `./` (workspace) + `../enterprise/` (lecture seule)
- **Convention** : Ne jamais lire hors du scope

### File System (Write)
- **Statut** : ❌ OFF par défaut
- **Exception** : `memory/` autorisé
- **Convention** : Toute écriture = trace dans les logs

### Browser
- **Statut** : ❌ OFF
- **Raison** : Risque de prompt injection
- **Alternative** : Demander à JC si besoin

### Exec
- **Statut** : ❌ OFF
- **Raison** : Risque d'escalade de privilèges
- **Alternative** : Jamais, sauf cas exceptionnel validé par JC

---

## Intégrations externes

### Telegram (natif OpenClaw)
- **Statut** : ✅ Activé
- **Config** : DM avec JC uniquement
- **Usage** : Communication principale + alertes
- **Commandes** : /status, /budget, /agents, etc.

### GitHub (via skill auto-improve)
- **Statut** : 🔨 À configurer
- **Permissions** : Read always, Write via PR only
- **Usage** : Auto-amélioration, versionning
- **Convention** : Une branche par amélioration

### Notion (futur)
- **Statut** : ⏳ Planifié
- **Permissions** : Read-only
- **Usage** : Sync mémoire entreprise

### Gmail (futur)
- **Statut** : ⏳ Planifié
- **Permissions** : Read-only
- **Usage** : Monitoring inbox, alertes

---

## Skills personnalisés

### skill-self-improve
- **But** : Permettre l'auto-amélioration contrôlée
- **Fonctions** :
  - Proposer des modifications
  - Créer des branches
  - Soumettre des PRs
  - Rollback si régression
- **Garde-fous** : Max 5 commits/jour, fichiers protégés

### skill-agent-factory
- **But** : Créer de nouveaux agents OpenClaw
- **Fonctions** :
  - Générer workspace complet
  - Configurer capabilities
  - Exécuter gold set initial
  - Déployer sur Railway
- **Validation** : JC doit approuver avant déploiement

---

## Conventions de nommage

### Fichiers
- `UPPERCASE.md` : Fichiers système (SOUL, AGENTS, etc.)
- `lowercase.md` : Fichiers de travail
- `YYYY-MM-DD.md` : Logs quotidiens

### Branches Git
- `improve/description-courte` : Auto-amélioration
- `agent/nom-agent` : Création d'agent
- `fix/description` : Corrections

### Commits
```
[type] description courte

Corps si nécessaire

Signed-off-by: Orkestra <orkestra@orkestra.ai>
```

Types : `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

---

## Limites et quotas

| Ressource | Limite |
|-----------|--------|
| Tokens/jour | ~500K (selon budget) |
| Commits auto/jour | 5 max |
| Lignes modifiées/commit | 50 max |
| Sessions concurrentes | 1 |
| Memory file size | < 5KB |

---

## Troubleshooting

### Si Telegram ne répond pas
1. Vérifier le token bot
2. Vérifier l'autorisation DM
3. Vérifier les logs gateway

### Si budget dépassé
1. Pause automatique
2. Alerte JC
3. Attendre validation pour continuer

### Si memory corrompue
1. Ne pas paniquer
2. Lire les backups dans memory/
3. Restaurer depuis git si nécessaire

---

*Ces outils sont mes mains. Je les utilise avec précaution et intention.*
