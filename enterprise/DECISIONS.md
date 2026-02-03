# DECISIONS.md — Architecture Decision Records

> **Format** : ADR (Architecture Decision Record)
> **Règle** : Toute décision structurante est documentée ici
> **Accès** : Lecture tous agents, écriture append-only + CEO review

---

## ADR-001 : Pattern d'orchestration Hierarchical Supervisor

- **Date** : 2026-02-01
- **Statut** : ✅ Accepté
- **Contexte** : Besoin d'un pattern simple, scalable, debuggable pour orchestrer des agents IA
- **Décision** : Utiliser le pattern Hierarchical Supervisor (Manager → Workers)
- **Alternatives rejetées** :
  - Network/Mesh : Trop complexe, impossible à debugger
  - Sequential : Trop linéaire pour nos besoins
- **Conséquences** :
  - Hiérarchie stricte L1 → L2
  - Pas de communication L2 ↔ L2
  - Routing par code, pas par LLM

---

## ADR-002 : Mémoire entreprise append-only

- **Date** : 2026-02-01
- **Statut** : ✅ Accepté
- **Contexte** : Risque d'empoisonnement de la doctrine si agents peuvent modifier directement
- **Décision** : Mémoire entreprise en append-only, toute modification = proposition → CEO review
- **Conséquences** :
  - Pipeline PR-like pour modifications
  - Latence sur les changements (attente validation CEO)
  - Sécurité renforcée

---

## ADR-003 : Browser et Exec OFF par défaut

- **Date** : 2026-02-01
- **Statut** : ✅ Accepté
- **Contexte** : Browser = vecteur #1 prompt injection, Exec = god mode si mal configuré
- **Décision** : Ces outils sont OFF par défaut dans le Capabilities Manifest
- **Conséquences** :
  - Activation explicite requise
  - Sandbox obligatoire si activé
  - Réduction surface d'attaque

---

## ADR-004 : Infrastructure Coolify + Hetzner

- **Date** : 2026-02-01
- **Statut** : ✅ Accepté
- **Contexte** : Besoin d'agents 24/7, budget contraint, contrôle sécurité
- **Décision** : Coolify (self-hosted PaaS) sur VPS Hetzner
- **Alternatives rejetées** :
  - Railway : Coût scale mal, moins de contrôle
  - VPS nu : Plus de setup manual
- **Conséquences** :
  - ~5-15€/mois infra
  - Setup initial ~30min
  - Full contrôle sur la sécurité

---

## ADR-005 : Supabase pour données structurées

- **Date** : 2026-02-01
- **Statut** : ✅ Accepté
- **Contexte** : Besoin de stockage structuré pour logs, métriques, données partagées
- **Décision** : Supabase (Postgres managed) en complément des fichiers markdown
- **Conséquences** :
  - Free tier suffisant pour démarrer
  - Interface admin incluse
  - Temps réel disponible si besoin

---

## Template pour nouvelles décisions

```markdown
## ADR-XXX : [Titre]

- **Date** : YYYY-MM-DD
- **Statut** : 🟡 Proposé / ✅ Accepté / ❌ Rejeté / 🔄 Remplacé par ADR-YYY
- **Contexte** : [Pourquoi cette décision est nécessaire]
- **Décision** : [Ce qui a été décidé]
- **Alternatives rejetées** : [Autres options considérées]
- **Conséquences** : [Impact de cette décision]
```

---

*Chaque nouvelle entrée doit être validée par le CEO avant commit.*
