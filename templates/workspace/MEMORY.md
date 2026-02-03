# MEMORY.md — [AGENT-ID]

> Mémoire long-terme de l'agent

---

## 📋 Format

Chaque entrée suit ce format :

```markdown
### [YYYY-MM-DD HH:MM] — [Type]

**Contexte** : [Situation]
**Action** : [Ce qui a été fait]
**Résultat** : [Outcome]
**Apprentissage** : [Ce qu'il faut retenir]

---
```

Types valides : `DÉCISION`, `ERREUR`, `PATTERN`, `PRÉFÉRENCE`, `CONTEXTE`

---

## 🧠 Mémoire active

<!-- Les entrées les plus récentes et pertinentes -->

---

## 📦 Archive

<!-- Entrées anciennes, conservées pour référence -->

---

## 🔗 Liens mémoire entreprise

Références aux documents enterprise/ pertinents pour cet agent :

| Document | Section | Pertinence |
|----------|---------|------------|
| STRATEGY.md | ... | ... |
| DECISIONS.md | ADR-XXX | ... |
| STANDARDS.md | ... | ... |

---

## ⚠️ Règles

1. **Append-only** : Jamais supprimer d'entrées
2. **Horodatage** : Toujours inclure date/heure
3. **Concision** : Max 5 lignes par entrée
4. **Pertinence** : Ne logger que ce qui sera utile plus tard

---

*Cette mémoire est propre à l'agent. Pour la mémoire partagée, voir enterprise/KNOWLEDGE/*
