import pytest
from text_preprocessing import tokenizer_fct

# Exemple de données pour les tests
test_sentence = "This is a test sentence for nltk preprocessing!"

# Test pour tokenizer_fct
def test_tokenizer_fct():
    tokens = tokenizer_fct(test_sentence)
    assert isinstance(tokens, list), "Le résultat doit être une liste"
    assert all(isinstance(token, str) for token in tokens), "Tous les éléments de la liste doivent être des chaînes de caractères"


