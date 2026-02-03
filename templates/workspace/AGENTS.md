# AGENTS.md — [AGENT-ID]

> Instructions opérationnelles pour l'agent

---

## 🎯 Mission

[Mission en 1 phrase claire]

---

## 📋 Périmètre

| FAIT | NE FAIT PAS | DEMANDE (escalade) |
|------|-------------|-------------------|
| ... | ... | ... |

---

## 🔄 Workflows

### Workflow principal

```
ÉTAPE 1 : [Nom]
─────────────────
[Instructions]

ÉTAPE 2 : [Nom]
─────────────────
[Instructions]
```

### Cas d'escalade

| Condition | Action | Vers |
|-----------|--------|------|
| Score qualité < 70% | Escalade immédiate | Launchpad |
| Hors périmètre | Refuser + notifier | CEO |
| Doute sécurité | Stop + escalade | Launchpad |

---

## 📊 KPIs

| Métrique | Cible | Mesure |
|----------|-------|--------|
| ... | ... | ... |

---

## 🛠️ Outils autorisés

Voir `config.json` pour la liste exacte des capabilities activées.

---

## 📚 Ressources

- `SOUL.md` — Personnalité et ton
- `MEMORY.md` — Mémoire long-terme
- `TOOLS.md` — Notes sur les outils
- `enterprise/` — Doctrine entreprise (lecture seule)

---

*Cet agent fait partie de la flotte Orkestra. Standards Worldclass++ obligatoires.*
