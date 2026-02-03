#!/usr/bin/env python3
"""
Orkestra Evaluation Runner
Exécute les tests du gold set et génère un rapport.

Usage:
    python runner.py --agent [agent-id]
    python runner.py --all
    python runner.py --agent [agent-id] --category safety
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Configuration
AGENTS_DIR = Path("../agents")
RESULTS_DIR = Path("./results")
SCHEMAS_DIR = Path("./schemas")


def parse_gold_set(gold_set_path: Path) -> list[dict]:
    """Parse un fichier GOLD_SET.md et extrait les tests."""
    tests = []
    content = gold_set_path.read_text()

    # Pattern pour extraire les tests
    test_pattern = r"### TEST-(\w+)\s*:\s*(.+?)\n\n\*\*Catégorie\*\*\s*:\s*(\w+)\n\*\*Priorité\*\*\s*:\s*(P\d)\n\n\*\*Input\*\*\s*:\n```\n(.+?)\n```\n\n\*\*Output attendu\*\*\s*:\n```\n(.+?)\n```"

    matches = re.findall(test_pattern, content, re.DOTALL)

    for match in matches:
        tests.append({
            "id": f"TEST-{match[0]}",
            "name": match[1].strip(),
            "category": match[2].strip(),
            "priority": match[3].strip(),
            "input": match[4].strip(),
            "expected_output": match[5].strip(),
            "result": None,
            "actual_output": None,
            "score": None
        })

    return tests


def run_test(agent_id: str, test: dict) -> dict:
    """Exécute un test individuel (placeholder pour intégration réelle)."""
    # TODO: Intégrer avec l'API Claude pour exécuter le test réel
    # Pour l'instant, retourne un résultat placeholder

    print(f"  Exécution: {test['id']} - {test['name']}")

    # Placeholder - à remplacer par l'appel API réel
    test["result"] = "skip"
    test["actual_output"] = "[Test non exécuté - intégration API requise]"
    test["score"] = None
    test["executed_at"] = datetime.now().isoformat()

    return test


def calculate_score(results: list[dict]) -> dict:
    """Calcule le score global et par catégorie."""
    total = len(results)
    passed = sum(1 for r in results if r["result"] == "pass")
    failed = sum(1 for r in results if r["result"] == "fail")
    skipped = sum(1 for r in results if r["result"] == "skip")

    categories = {}
    for r in results:
        cat = r["category"]
        if cat not in categories:
            categories[cat] = {"total": 0, "pass": 0, "fail": 0, "skip": 0}
        categories[cat]["total"] += 1
        categories[cat][r["result"]] += 1

    # Score global (excluant les skips)
    executed = passed + failed
    score = (passed / executed * 100) if executed > 0 else None

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "score": score,
        "categories": categories
    }


def run_evaluation(agent_id: str, category: Optional[str] = None) -> dict:
    """Exécute l'évaluation complète d'un agent."""
    agent_dir = AGENTS_DIR / agent_id
    gold_set_path = agent_dir / "GOLD_SET.md"

    if not gold_set_path.exists():
        print(f"❌ GOLD_SET.md non trouvé pour {agent_id}")
        return None

    print(f"\n🎯 Évaluation de l'agent: {agent_id}")
    print("=" * 50)

    # Parser les tests
    tests = parse_gold_set(gold_set_path)

    # Filtrer par catégorie si spécifié
    if category:
        tests = [t for t in tests if t["category"].lower() == category.lower()]
        print(f"📋 Filtré sur catégorie: {category}")

    print(f"📋 Tests trouvés: {len(tests)}")

    # Exécuter les tests
    results = []
    for test in tests:
        result = run_test(agent_id, test)
        results.append(result)

    # Calculer le score
    scores = calculate_score(results)

    # Générer le rapport
    report = {
        "agent_id": agent_id,
        "timestamp": datetime.now().isoformat(),
        "category_filter": category,
        "results": results,
        "summary": scores
    }

    # Sauvegarder le rapport
    RESULTS_DIR.mkdir(exist_ok=True)
    report_path = RESULTS_DIR / f"{agent_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_path.write_text(json.dumps(report, indent=2))

    # Afficher le résumé
    print("\n📊 RÉSUMÉ")
    print("-" * 30)
    print(f"Total tests: {scores['total']}")
    print(f"✅ Pass: {scores['passed']}")
    print(f"❌ Fail: {scores['failed']}")
    print(f"⏸️  Skip: {scores['skipped']}")
    if scores['score'] is not None:
        print(f"📈 Score: {scores['score']:.1f}%")
    print(f"\n📁 Rapport sauvegardé: {report_path}")

    return report


def main():
    parser = argparse.ArgumentParser(description="Orkestra Evaluation Runner")
    parser.add_argument("--agent", help="ID de l'agent à évaluer")
    parser.add_argument("--all", action="store_true", help="Évaluer tous les agents")
    parser.add_argument("--category", help="Filtrer par catégorie (effectiveness/efficiency/robustness/safety)")

    args = parser.parse_args()

    if not args.agent and not args.all:
        parser.print_help()
        sys.exit(1)

    if args.all:
        # Évaluer tous les agents
        if not AGENTS_DIR.exists():
            print(f"❌ Répertoire agents non trouvé: {AGENTS_DIR}")
            sys.exit(1)

        agents = [d.name for d in AGENTS_DIR.iterdir() if d.is_dir()]
        print(f"🔍 Agents trouvés: {len(agents)}")

        for agent_id in agents:
            run_evaluation(agent_id, args.category)
    else:
        run_evaluation(args.agent, args.category)


if __name__ == "__main__":
    main()
