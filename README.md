# api-nlp-tags

## Description
Bienvenue sur le dépôt de l'API Flask api-nlp-tags. Cette API est conçue pour prédire des tags en fonction d'une question posée sur le site StackOverFlow. Elle utilise le modèle de Machine Learning SGDClassifier et la technologie Flask.

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
