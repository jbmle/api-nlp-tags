import streamlit as st
from model_module import TagPredictor

# Création d'une instance du modèle
model = TagPredictor()

st.title("Prédicteur de Tags")

# Champ de texte pour la question
question = st.text_input("Entrez votre question")

# Bouton pour soumettre la question
if st.button('Prédire'):
    if question:
        tags = model.predire_tags(question)
        st.write("Tags prédits:")
        for tag in tags:
            st.write(f"- {tag}")
    else:
        st.error("Veuillez entrer une question.")
