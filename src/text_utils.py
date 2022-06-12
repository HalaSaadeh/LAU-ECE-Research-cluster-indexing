# imports
import nltk
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer 
from nltk.tokenize import word_tokenize
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


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


def textToDataFrame(content):
    """
    Converts text to a data-frame of tf-idf vectors

    Args:
        - content: input text
    Returns:
        - df1: dataframe of tf-idf vectors
        - list_FeatureKeys: feature names of the tf-idf vectors
    """
    vectorizer = TfidfVectorizer(ngram_range=(1, 1))
    vectors = vectorizer.fit_transform(content[0:len(content)])
    list_FeatureKeys = vectorizer.get_feature_names_out()
    dense = vectors.todense()
    denselist = dense.tolist()
    df1 = pd.DataFrame(denselist, columns=list_FeatureKeys)
    return df1, list_FeatureKeys
