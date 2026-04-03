# 📐 Data Specifications — Livraison Membre 2

> Document de référence pour l'interface entre le pipeline data (Membre 1) et le modèle IA (Membre 2).  
> **Ne pas modifier sans concertation.**

---

## Format des fichiers livrés

| Fichier | Contenu | Shape |
|---------|---------|-------|
| `X_train.npy` | Features d'entraînement | `(n, 30, 258)` |
| `X_val.npy` | Features de validation | `(n, 30, 258)` |
| `X_test.npy` | Features de test | `(n, 30, 258)` |
| `y_train.npy` | Labels entiers train | `(n,)` |
| `y_val.npy` | Labels entiers val | `(n,)` |
| `y_test.npy` | Labels entiers test | `(n,)` |
| `labels.json` | Mapping index → classe | — |

---

## Détail des 258 features par frame

| Partie du corps | Landmarks | Valeurs/landmark | Total |
|-----------------|-----------|-----------------|-------|
| Pose (corps) | 33 | 4 (x, y, z, visibility) | 132 |
| Main gauche | 21 | 3 (x, y, z) | 63 |
| Main droite | 21 | 3 (x, y, z) | 63 |
| **Total** | | | **258** |

---

## Conventions

- Coordonnées normalisées entre 0 et 1 (relatives à la taille de l'image)
- Valeurs manquantes (main non détectée) = vecteur de **zéros**
- Séquences standardisées à **30 frames** par interpolation
- Split : **70% train / 15% val / 15% test** (stratifié par classe)
- Encodage des labels : **entiers** (0 à 19), voir `labels.json`

---

## Labels mapping

```json
{
  "eat": 0, "drink": 1, "water": 2, "sleep": 3, "medicine": 4,
  "hello": 5, "please": 6, "thank_you": 7, "sorry": 8, "goodbye": 9,
  "yes": 10, "no": 11, "help": 12, "who": 13, "what": 14,
  "home": 15, "school": 16, "mother": 17, "father": 18, "friend": 19
}
```

---

## Chemin Google Drive

```
Drive/SignLanguage_Project/02_Dataset_Final/
├── X_train.npy
├── X_val.npy
├── X_test.npy
├── y_train.npy
├── y_val.npy
├── y_test.npy
└── labels.json
```
