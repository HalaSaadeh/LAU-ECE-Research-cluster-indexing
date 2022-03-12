# imports
import nltk


# constants
LANGUAGE = "english"


def stopword_removal():
    stopwords = set(nltk.corpus.stopwords.words(LANGUAGE))
    
    stopwords.update([',', '.', '_', '(', ')', ':', '%', '_', '"'])
    stopwords.update(['percent','cent','per','wbgs','pcbs','dv','vaw'])
    stopwords.update(['january', 'february', 'march', 'april', 'may', 'june',
                    'july', 'august', 'september', 'october', 'november', 'december'])
    
    
    return stopwords
