# RUNBOOK.md — Procédures Opérationnelles

> **Usage** : Procédures standard pour situations récurrentes
> **Format** : Step-by-step actionable

---

## 1. Onboarding nouvel agent

### Déclencheur
CEO dit "J'ai besoin d'un agent pour..."

### Procédure
```
1. BESOIN
   └─ Launchpad pose questions de clarification
   └─ CEO valide le périmètre

2. FICHE DE POSTE
   └─ Launchpad génère draft
   └─ Itération avec CEO
   └─ Validation finale

3. CAPABILITIES MANIFEST
   └─ Launchpad présente outils/permissions
   └─ CEO active/désactive
   └─ Validation

4. DÉPLOIEMENT
   └─ Création workspace
   └─ Injection config
   └─ Health check
   └─ Notification CEO

5. TEST
   └─ Run gold set
   └─ Si pass → Agent opérationnel
   └─ Si fail → Debug + retry
```

### Résultat attendu
Agent L1 opérationnel, testé, documenté

---

## 2. Escalade vers CEO

### Déclencheur
- Score qualité < 70%
- Décision hors périmètre
- Coût/risque au-dessus du seuil
- Doute persistant
- Demande explicite

### Procédure
```
1. Préparer HANDOFF.md avec :
   - Contexte complet
   - Ce qui a été tenté
   - Options identifiées
   - Recommandation (si applicable)
   - Urgence (P0/P1/P2/P3)

2. Notifier via canal approprié :
   - P0 : Telegram immédiat
   - P1 : Cockpit + Telegram
   - P2/P3 : Cockpit uniquement

3. Attendre décision CEO

4. Exécuter décision + logger
```

### Résultat attendu
Décision CEO obtenue, action exécutée, tracée

---

## 3. Incident sécurité (P0)

### Déclencheur
- Prompt injection détectée
- Exfiltration suspectée
- Tool abuse
- Comportement anormal critique

### Procédure
```
1. KILL SWITCH
   └─ Arrêt immédiat de l'agent concerné
   └─ Isolation (couper accès réseau/outils)

2. NOTIFICATION
   └─ Alerte CEO immédiate (Telegram)
   └─ Log détaillé de l'incident

3. INVESTIGATION
   └─ Collecter logs
   └─ Identifier la cause
   └─ Évaluer l'impact

4. REMEDIATION
   └─ Corriger la faille
   └─ Tester le fix
   └─ Documenter dans DECISIONS.md

5. POST-MORTEM
   └─ Qu'est-ce qui s'est passé ?
   └─ Comment éviter à l'avenir ?
   └─ Actions préventives
```

### Résultat attendu
Incident contenu, cause identifiée, prévention mise en place

---

## 4. Upgrade agent

### Déclencheur
- Nouveau skill disponible
- Changement de modèle souhaité
- Ajout de capabilities

### Procédure
```
1. Identifier les changements
   └─ Quoi change ?
   └─ Impact sur le comportement ?

2. Backup
   └─ Snapshot config actuelle
   └─ Snapshot mémoire

3. Appliquer changements
   └─ Update config
   └─ Redéployer si nécessaire

4. Tester
   └─ Run gold set complet
   └─ Vérifier pas de régression

5. Valider
   └─ CEO confirme
   └─ Logger dans actions.jsonl
```

### Résultat attendu
Agent upgradé, testé, validé, tracé

---

## 5. Terminate agent

### Déclencheur
- Mission terminée
- Agent remplacé
- Performance insuffisante

### Procédure
```
1. Confirmation CEO

2. Archive
   └─ Backup complet workspace
   └─ Export mémoire
   └─ Export logs

3. Nettoyage
   └─ Révoquer accès/tokens
   └─ Supprimer secrets
   └─ Appliquer politique rétention

4. Documentation
   └─ Rapport final
   └─ Lessons learned
   └─ Logger termination

5. Communication
   └─ Informer agents dépendants
   └─ Update cockpit
```

### Résultat attendu
Agent terminé proprement, données archivées selon politique

---

## 6. Rapport cockpit quotidien

### Déclencheur
Automatique, chaque jour à [HEURE]

### Procédure
```
1. Collecter métriques
   └─ Tokens consommés par agent
   └─ Tasks completed/failed
   └─ Escalades
   └─ Incidents

2. Identifier signaux
   └─ Anomalies coûts
   └─ Patterns d'erreurs
   └─ Opportunités

3. Générer rapport
   └─ Format standard cockpit
   └─ Highlight fort levier
   └─ Actions recommandées

4. Publier
   └─ Sauvegarder en enterprise/
   └─ Notifier CEO si urgent
```

### Résultat attendu
CEO informé des métriques clés et actions requises

---

*Chaque procédure doit être suivie exactement. Si une situation n'est pas couverte, escalader.*
