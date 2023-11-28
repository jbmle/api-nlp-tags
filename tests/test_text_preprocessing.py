import pytest
from text_preprocessing import tokenizer_fct, lower_start_fct, lemma_fct

# Exemple de données pour les tests
test_sentence = "This is a test sentence for nltk preprocessing!"

# Test pour tokenizer_fct
def test_tokenizer_fct():
    tokens = tokenizer_fct(test_sentence)
    assert isinstance(tokens, list), "Le résultat doit être une liste"
    assert all(isinstance(token, str) for token in tokens), "Tous les éléments de la liste doivent être des chaînes de caractères"

def test_lower_start_fct():
    tokens = tokenizer_fct(test_sentence)
    lower_tokens = lower_start_fct(tokens)
    assert all(token.islower() or not token.isalpha() for token in lower_tokens), "Tous les tokens doivent être en minuscules"

def test_lemma_fct():
    tokens = tokenizer_fct(test_sentence)
    lemmatized_tokens = lemma_fct(tokens)
    assert len(lemmatized_tokens) == len(tokens), "Le nombre de tokens doit rester le même après lemmatisation"
