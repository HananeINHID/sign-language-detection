# 🤟 Sign Language Detection Project

## 📌 Description

Ce projet a pour objectif de développer un système de détection de la langue des signes basé sur la vision par ordinateur et le machine learning. Il permet de reconnaître en temps réel les gestes de la main à partir d’une webcam ou d’images, et de les traduire en texte ou en commandes.

## 🎯 Objectifs

* Détecter la main dans une image ou un flux vidéo
* Extraire les points clés (landmarks) de la main
* Classifier les gestes correspondant à des signes
* Afficher la prédiction en temps réel

## 🛠️ Technologies utilisées

* Python
* OpenCV (traitement d’image)
* MediaPipe (détection des mains et landmarks)
* TensorFlow / Keras ou Scikit-learn (modèle de classification)
* NumPy, Pandas (manipulation des données)

## 📂 Structure du projet

```
sign-language-detection/
│
├── data/                # Dataset des images/gestes
├── models/              # Modèles entraînés
├── src/
│   ├── detection.py     # Détection de la main
│   ├── preprocessing.py # Prétraitement des données
│   ├── train.py         # Entraînement du modèle
│   ├── predict.py       # Prédiction en temps réel
│
├── requirements.txt
├── README.md
└── main.py              # Script principal
```

## ⚙️ Installation

1. Cloner le projet :

```bash
git clone https://github.com/username/sign-language-detection.git
cd sign-language-detection
```

2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

## ▶️ Utilisation

Lancer la détection en temps réel :

```bash
python main.py
```

Le programme va :

* Activer la webcam
* Détecter la main
* Identifier le signe
* Afficher le résultat à l’écran

## 🧠 Fonctionnement

1. Capture vidéo via webcam
2. Détection de la main avec MediaPipe
3. Extraction des coordonnées des points clés
4. Passage dans un modèle de classification
5. Affichage du signe reconnu

## 🤝 Contribution

Les contributions sont les bienvenues :

* Fork du projet
* Création d’une branche
* Pull request

## 📜 Licence

Ce projet est open-source et disponible sous licence MIT.

## 👨‍💻 Auteur

* OUHAMMOU Youssef
* Inhid Hanane
* Ait bilfakih Asmae 

---

💡 *Ce projet vise à faciliter la communication avec les personnes malentendantes grâce à l’intelligence artificielle.*
