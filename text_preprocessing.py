# imports
from operator import imod
import nltk
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer 

# constants
LANGUAGE = "english"

porter = PorterStemmer()
snow_stemmer = SnowballStemmer(language='english')


def stopword_removal():
    '''
    Removes stopwords from the 
    
    Returns:
        - new stopword set of type 'set' that contains all relevant stopwords.

    
    '''
    
    stopwords = set(nltk.corpus.stopwords.words(LANGUAGE))
    
    stopwords.update([',', '.', '_', '(', ')', ':', '%', '_', '"'])
    stopwords.update(['percent','cent','per','wbgs','pcbs','dv','vaw'])
    stopwords.update(['january', 'february', 'march', 'april', 'may', 'june',
                    'july', 'august', 'september', 'october', 'november', 'december'])
    
    
    return stopwords


def lemmatization():
    lemma = nltk.wordnet.WordNetLemmatizer()
