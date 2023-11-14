import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
import joblib
from text_preprocessing import transform_bow


class TagPredictor:
    def __init__(self):
        try:
            self.vectorizer = joblib.load('models/tfidf_vectorizer.joblib')
            self.mlb = joblib.load('models/multilabel_binarizer.joblib')
            self.model = joblib.load('models/sgd_classifier_model.joblib')
        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des modèles : {e}")
           

    def pretraiter_question(self, question):
        question_cleaned = transform_bow(question)
        question_cleaned = question_cleaned.split()
        return question_cleaned

    def predire_tags(self, question):
        question_cleaned = self.pretraiter_question(question)
        print(f"Question cleaned: {question_cleaned}")

        question_vect = self.vectorizer.transform([question_cleaned])
        proba_tags = self.model.predict_proba(question_vect)

        top5_indices = np.argsort(proba_tags, axis=1)[:, -5:]

        tags = self.mlb.classes_[top5_indices.flatten()]

        return list(tags)

    

    