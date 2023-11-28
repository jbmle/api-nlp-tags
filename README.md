# api-nlp-tags

## Description
Bienvenue sur le dépôt de l'API Flask api-nlp-tags. Cette API est conçue pour prédire des tags en fonction d'une question posée sur le site StackOverFlow. Elle utilise le modèle de Machine Learning SGDClassifier et la technologie Flask.

## Détail des dossiers et fichiers
- Le dossier models contient les fichiers joblib issus des modèles de ML entraînés au préalable dans le notebook de modèle supervisé.  
- Le dossier tests contient les tests unitaires à utiliser avec pytest.  
- Le fichier app.py définit la route pour faire une requête POST et obtenir une liste de tags en fonction d'une question posée.  
- Le fichier model_module.py applique le modèle SGDClassifier grâce aux fichiers du dossier models.
- Le fichier text_preprocessing.py reprend le nettoyage du texte effectué dans le notebook d'exploration, pour notamment tokeniser et lemmatiser la question fournie à l'api.
- Le fichier requirements.txt liste les dépendances liées au projet.


## Installation
Pour installer et exécuter cette API localement, suivez ces étapes :

1. **Cloner le dépôt** :
`git clone https://github.com/jbmle/api-nlp-tags.git`

2. **Installer les Dépendances** :
`pip install -r requirements.txt`

3. **Lancer l'API Flask** :
`python3 app.py`


## Utilisation
Après avoir lancé l'API, envoyez une requête POST à `/predict` avec une question pour obtenir des tags prédictifs.

`curl -X POST -H "Content-Type: application/json" -d '{"question": "posez votre question"}' http://localhost:5000/predict`

## Tests
Pour exécuter les tests, utilisez :
`pytest tests/`
