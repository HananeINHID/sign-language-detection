# 📐 Data Specifications — Livraison Finale

> Document de référence pour l'interface entre le pipeline data (Membre 1) et le modèle IA (Membre 2).  
> **Ne pas modifier sans concertation.**

---

## 📊 Résumé du Dataset

- **Total vidéos :** 45 (moyenne de 9 vidéos/classe)
- **Classes :** 5 (`eat`, `drink`, `water`, `sleep`, `medicine`)
- **Shape d'entrée :** `(64, 1662)` 
- **Split :** 70% train (31 vidéos) / 15% val (7 vidéos) / 15% test (7 vidéos)

---

## ⚠️ Note importante pour Membre 2 (Modélisation)

Le volume de données actuel est très limité. Voici les recommandations techniques pour compenser ce faible nombre d'échantillons lors de l'entraînement :
- **Data Augmentation fortement recommandée :** Appliquer des transformations sur les coordonnées (flip horizontal, ajout de bruit gaussien temporel ou spatial).
- **Architecture :** Réduire drastiquement la complexité du modèle pour éviter un surapprentissage (overfitting) immédiat. Privilégier des réseaux légers.
- **Attentes :** Ne pas s'attendre à une *accuracy* supérieure à 80% en validation/test sur ce volume de données brut.

---

## Format des fichiers livrés (Vérification Finale OK ✅)

| Fichier | Contenu | Shape |
|---------|---------|-------|
| `X_train.npy` | Features d'entraînement | `(31, 64, 1662)` |
| `X_val.npy` | Features de validation | `(7, 64, 1662)` |
| `X_test.npy` | Features de test | `(7, 64, 1662)` |
| `y_train.npy` | Labels entiers train | `(31,)` |
| `y_val.npy` | Labels entiers val | `(7,)` |
| `y_test.npy` | Labels entiers test | `(7,)` |
| `labels.json` | Mapping index → classe | — |

*Note : Aucune valeur `NaN` n'est présente dans les jeux de données.*

---

## Détail des 1662 features par frame

| Partie du corps | Landmarks | Valeurs/landmark | Total |
|-----------------|-----------|-----------------|-------|
| Pose (corps) | 33 | 4 (x, y, z, visibility) | 132 |
| Face (visage) | 468 | 3 (x, y, z) | 1404 |
| Main gauche | 21 | 3 (x, y, z) | 63 |
| Main droite | 21 | 3 (x, y, z) | 63 |
| **Total** | | | **1662** |

---

## Conventions

- Coordonnées normalisées entre 0 et 1 (relatives à la taille de l'image).
- Valeurs manquantes (ex: main non détectée ou hors cadre) = vecteur de **zéros**.
- Séquences standardisées à **64 frames** par interpolation ou padding.
- Encodage des labels : **entiers** (0 à 4), voir `labels.json`.

---

## Labels mapping

```json
{
  "eat": 0, 
  "drink": 1, 
  "water": 2, 
  "sleep": 3, 
  "medicine": 4
}                                                                                                    
## Chemin Google Drive

```
Drive/MyDrive/Projets/sign-language-detection/02_Dataset_Final/
├── X_train.npy
├── X_val.npy
├── X_test.npy
├── y_train.npy
├── y_val.npy
├── y_test.npy
└── labels.json
```