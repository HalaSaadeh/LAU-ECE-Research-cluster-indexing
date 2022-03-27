# imports
import nltk
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer 
from nltk.tokenize import word_tokenize
import re

# constants
LANGUAGE = "english"

porter = PorterStemmer()
snow_stemmer = SnowballStemmer(language='english')


def stopword_removal(text):
    """
    Removes stopwords from text

    Args:
        - text: input text
    Returns:
        - filtered text without stopwords
    """
    
    stopwords = set(nltk.corpus.stopwords.words(LANGUAGE))
    
    stopwords.update([',', '.', '_', '(', ')', ':', '%', '_', '"'])
    stopwords.update(['percent','cent','per','wbgs','pcbs','dv','vaw'])
    stopwords.update(['january', 'february', 'march', 'april', 'may', 'june',
                      'july', 'august', 'september', 'october', 'november', 'december'])

    text = text.lower()
    tokenizedText = word_tokenize(text)
    filteredText = [w for w in tokenizedText if (not (w.lower() in stopwords) and w.isalpha())]
    return filteredText


def lemmatization(word):
    """
    Performs lemmatization on a single word

    Args:
        - word: input word
    Returns:
        - lemmatized word
    """
    lemma = nltk.wordnet.WordNetLemmatizer()
    return lemma.lemmatize(word)


def hasNumbers(inputString):
    """
    Checks whether the input string has numbers
    Args:
        - inputString: input string
    Returns:
        - bool true or false
    """
    return bool(re.search(r'\d', inputString))


def stemming(text):
    """
    Performs stemming on input text

    Args:
        - text: input text
    Returns:
        - stemmed text
    """
    stemmedText = []
    for word in text:
        if not hasNumbers(word) and len(word)>2:
            stemmedText.append(lemmatization(word))
    return stemmedText


