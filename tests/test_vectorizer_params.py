import pytest
from model_module import TagPredictor

@pytest.fixture
def tag_predictor():
    # Cette fonction setup crée une nouvelle instance du prédicteur pour chaque test
    return TagPredictor()

def test_vectorizer_max_df(tag_predictor):
    assert tag_predictor.vectorizer.get_params()['max_df'] == 0.6, "max_df is incorrect!"

# Test général
def test_vectorizer_params(tag_predictor):
    params = tag_predictor.vectorizer.get_params()
    expected_params = {
        'max_df': 0.6,
        # ...
    }
    for param, expected_value in expected_params.items():
        assert params[param] == expected_value, f"{param} is incorrect!"
