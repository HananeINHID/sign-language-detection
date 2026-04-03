# ✅ Quality Checklist — Avant chaque livraison

À cocher avant de partager les fichiers .npy avec Membre 2.

## Phase 1 — Vidéos brutes
- [ ] Chaque classe a au moins **30 vidéos**
- [ ] Au moins **2 signeurs différents** par classe
- [ ] Toutes les vidéos sont en **480p minimum**
- [ ] Aucune vidéo ne dure moins de **0.5 seconde**
- [ ] Le log `data_log.csv` est à jour

## Phase 2 — Extraction MediaPipe
- [ ] Taux d'échec de détection < 20% par vidéo
- [ ] Aucune séquence avec > 90% de valeurs à zéro
- [ ] Toutes les séquences sont à 30 frames

## Phase 3 — Dataset final
- [ ] Shape vérifiée : `(n, 30, 258)` pour X
- [ ] Aucun NaN ni Inf dans les arrays
- [ ] Distribution des classes vérifiée (aucune classe < 70% de la médiane)
- [ ] Split stratifié confirmé : 70 / 15 / 15
- [ ] `labels.json` présent et correct
- [ ] Rapport qualité `run_full_quality_report()` passé sans erreur

## Communication équipe
- [ ] Membre 2 notifié de la disponibilité des fichiers
- [ ] Chemin Drive communiqué
- [ ] `data_specs.md` partagé et validé
