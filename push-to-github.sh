#!/bin/bash
# Push MissionBound Railway vers GitHub
# À exécuter dans Railway SSH ou ton Mac

cd /tmp/missionbound-railway-fork

# Configure le remote
git remote remove origin 2>/dev/null
git remote add origin https://github.com/orkestra-ai-org/missionbound-railway.git

# Push (demandera ton token)
echo "Prêt à pousser vers orkestra-ai-org/missionbound-railway"
echo "Quand ça demande le mot de passe, utilise ton GitHub Personal Access Token"
echo ""
git push -u origin main
