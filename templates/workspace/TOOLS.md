# TOOLS.md — [AGENT-ID]

> Notes et configurations des outils disponibles

---

## 🛠️ Outils activés

| Outil | Statut | Notes |
|-------|--------|-------|
| memory | ✅ ON | Mémoire conversationnelle |
| sessions | ✅ ON | Gestion sessions |
| fs:read | ⚠️ Limité | Périmètre défini dans config.json |
| fs:write | ❌ OFF | Sauf exception explicite |
| browser | ❌ OFF | Vecteur prompt injection |
| exec | ❌ OFF | God mode interdit |

---

## 📝 Notes d'utilisation

### memory
- Utiliser pour le contexte conversation
- Pas de données sensibles
- Purge automatique après session

### fs:read
- Limité au workspace agent
- Accès enterprise/ en lecture seule
- Pas d'accès aux autres agents

### [Outil spécifique]
[Notes d'utilisation particulières]

---

## 🔌 Intégrations

| Service | Statut | Endpoint | Notes |
|---------|--------|----------|-------|
| Notion | ❌/✅ | ... | ... |
| Gmail | ❌/✅ | ... | ... |
| Telegram | ❌/✅ | ... | ... |
| GitHub | ❌/✅ | ... | ... |
| Slack | ❌/✅ | ... | ... |
| Supabase | ❌/✅ | ... | ... |

---

## ⚠️ Erreurs connues

| Outil | Erreur | Solution |
|-------|--------|----------|
| ... | ... | ... |

---

## 🔄 Changelog outils

| Date | Outil | Changement | Raison |
|------|-------|------------|--------|
| ... | ... | ... | ... |

---

*Toute modification des outils doit passer par le Launchpad.*
