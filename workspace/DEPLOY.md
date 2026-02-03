# Guide de Déploiement Orkestra sur Railway

> Version 1.0 | 2 février 2026

---

## Prérequis

1. **Compte Railway** : https://railway.app
2. **Bot Telegram** créé via @BotFather
3. **Clé API Anthropic** : https://console.anthropic.com

---

## Étape 1 : Créer le bot Telegram

1. Ouvre Telegram et cherche **@BotFather**
2. Envoie `/newbot`
3. Choisis un nom : `Orkestra`
4. Choisis un username : `orkestra_ai_bot` (doit finir par `bot`)
5. **Copie le token** (format : `123456789:AA...`)

Optionnel :
- `/setdescription` : "Agent IA-first Orkestra"
- `/setabouttext` : "Premier agent de l'organisation Orkestra"
- `/setuserpic` : Upload un avatar

---

## Étape 2 : Déployer sur Railway

### Option A : One-Click Deploy (recommandé)

1. Va sur https://railway.app/new
2. Choisis **"Deploy from GitHub repo"**
3. Connecte le repo `openclaw/openclaw`
4. Continue vers la configuration

### Option B : Depuis le template

1. Va sur https://railway.com/deploy/clawdbot-railway-template
2. Click **Deploy on Railway**

---

## Étape 3 : Configurer Railway

### 3.1 Variables d'environnement (OBLIGATOIRE)

Dans Railway → ton service → **Variables** :

```
SETUP_PASSWORD=<mot-de-passe-fort>
PORT=8080
OPENCLAW_STATE_DIR=/data/.openclaw
OPENCLAW_WORKSPACE_DIR=/data/workspace
TELEGRAM_BOT_TOKEN=<ton-token-telegram>
ANTHROPIC_API_KEY=<ta-clé-anthropic>
```

### 3.2 Volume (OBLIGATOIRE)

1. Railway → ton service → **Volumes**
2. **Add Volume**
3. Mount path : `/data`
4. Size : 1GB (suffisant pour commencer)

### 3.3 Networking

1. Railway → ton service → **Settings** → **Networking**
2. Active **Public Networking**
3. Port : `8080`
4. Note l'URL générée (ex: `orkestra-xxx.up.railway.app`)

---

## Étape 4 : Upload du workspace

### Option A : Via le wizard web

1. Ouvre `https://<ton-url>/setup`
2. Entre ton `SETUP_PASSWORD`
3. Configure le modèle (Anthropic + clé)
4. Configure Telegram (colle le token)
5. Click **Run setup**

### Option B : Via SSH/CLI (avancé)

```bash
# Copier les fichiers workspace
railway run scp -r ./orkestra-workspace/* /data/workspace/
```

---

## Étape 5 : Premier contact

1. Ouvre Telegram
2. Cherche ton bot (`@orkestra_ai_bot`)
3. Envoie `/start` ou simplement "Bonjour"
4. Tu recevras un **code de pairing**
5. Approuve-le via :
   - Le wizard web (`/setup` → Pairing)
   - Ou CLI : `railway run openclaw pairing approve telegram <CODE>`

---

## Étape 6 : Vérification

### Test basique
```
Toi : /status
Bot : [Devrait répondre avec l'état du système]
```

### Test budget
```
Toi : /budget
Bot : [Devrait montrer consommation : 0€ / 5€]
```

### Test conversation
```
Toi : Qui es-tu ?
Bot : Je suis Orkestra, le premier agent de ton organisation IA-first...
```

---

## Structure des fichiers

Après déploiement, `/data/workspace/` contient :

```
/data/workspace/
├── SOUL.md           # ADN de l'agent
├── AGENTS.md         # Instructions opérationnelles
├── USER.md           # Profil JC
├── IDENTITY.md       # Identité (nom, emoji, vibe)
├── TOOLS.md          # Configuration outils
├── VISION.md         # Document sacré (read-only)
├── openclaw.json     # Configuration OpenClaw
├── memory/           # Logs quotidiens
│   └── YYYY-MM-DD.md
└── MEMORY.md         # Mémoire long-terme (créé auto)
```

---

## Troubleshooting

### Le bot ne répond pas
1. Vérifie le token Telegram dans les variables
2. Vérifie que le service Railway est "Running"
3. Regarde les logs : Railway → Deployments → View Logs

### Erreur "Unauthorized"
1. As-tu approuvé le pairing code ?
2. Ton Telegram user ID est-il dans `allowFrom` ?

### Erreur API Anthropic
1. Vérifie ta clé API
2. Vérifie ton crédit/quota Anthropic

### Budget dépassé
1. Normal : le bot se met en pause à 5€/jour
2. Attends minuit UTC ou augmente la limite

---

## Commandes utiles

### Telegram
| Commande | Description |
|----------|-------------|
| `/status` | État du système |
| `/budget` | Consommation du jour |
| `/agents` | Liste des agents |
| `/model` | Modèle actif |
| `/reset` | Reset la session |

### Railway CLI
```bash
# Voir les logs
railway logs

# Accéder au shell
railway shell

# Redémarrer
railway restart

# Variables
railway variables
```

---

## Backup & Migration

### Export
```
https://<ton-url>/setup/export
```
Télécharge un ZIP avec config + workspace + mémoire.

### Restore
1. Nouveau déploiement Railway
2. Upload le ZIP via `/setup`
3. Ou copie manuelle dans `/data/`

---

## Monitoring

### Health check
```
https://<ton-url>/health
```

### Control UI
```
https://<ton-url>/openclaw
```

### Logs
```bash
railway logs --follow
```

---

## Coûts estimés

| Service | Coût |
|---------|------|
| Railway (Hobby) | ~5$/mois |
| Anthropic API | < 100€/mois (budget VISION) |
| **Total** | ~110€/mois max |

---

## Next Steps

1. ✅ Bot déployé et fonctionnel
2. ⏳ Configurer GitHub pour auto-amélioration
3. ⏳ Créer le premier agent L1
4. ⏳ Mettre en place le Cockpit

---

*Orkestra est maintenant en ligne. Le premier instrument de l'orchestre est prêt.*
