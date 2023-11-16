from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Téléchargement des ressources NLTK
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


def tokenizer_fct(sentence) :
    sentence_clean = sentence.replace('-', ' ').replace('/', ' ').replace("'", " ")
    word_tokens = word_tokenize(sentence_clean)
    return word_tokens

from nltk.corpus import stopwords
stop_w = list(set(stopwords.words('english'))) + ['[', ']', ',', '.', ':', '?', '(', ')']

def stop_word_filter_fct(list_words) :
    filtered_w = [w for w in list_words if not w in stop_w]
    filtered_w2 = [w for w in filtered_w if len(w) > 2]
    return filtered_w2

def lower_start_fct(list_words) :
    lw = [w.lower() for w in list_words if (not w.startswith("@")) 
                                       and (not w.startswith("http"))]
    return lw

def lemma_fct(list_words) :
    lemmatizer = WordNetLemmatizer()
    lem_w = [lemmatizer.lemmatize(w) for w in list_words]
    return lem_w

def filter_nouns(list_words):
    pos_tags = nltk.pos_tag(list_words)
    nouns = [word for word, pos in pos_tags if pos in ('NN', 'NNS', 'NNP', 'NNPS')]
    return nouns

def transform_bow(desc_text) :
    word_tokens = tokenizer_fct(desc_text)
    sw = stop_word_filter_fct(word_tokens)
    lw = lower_start_fct(sw)
    lem_w = lemma_fct(lw)    
    nn_w = filter_nouns(lem_w)    
    transf_desc_text = ' '.join(nn_w)
    return transf_desc_text