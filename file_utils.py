import glob

import pdftotext
import os
from text_utils import stopword_removal, stemming


def convert(lst):
    return ' '.join(lst)


def extractFromFile(file):
    """
    Extract the textual content from files.

    Args:
        - file: Local path to file
    Returns:
        - the textual content from the file
    """
    content = ""
    with open(file, "rb") as f:
        pdf = pdftotext.PDF(f)
        for page in pdf:
            content += page  # .encode('utf-8')

    print('File extracted!')
    return content


def extractDataset(datasetPath):
    """
    Extract the content from the dataset.

    Args:
        - datasetPath: local path to the dataset
    Returns:
        - content:
    """
    os.chdir(datasetPath)
    files = glob.glob("*.*")
    content = []
    filenames = []

    for file in files:
        if file.lower().endswith('.pdf'):
            filenames.append(str(file))
            filteredText = stopword_removal(extractFromFile(file))
            stems = stemming(filteredText)
            content.append(convert(stems))

    return content


# print(extractFromFile("D:/Research/SDG Corpus/goal_1.pdf"))
# extractDataset("D:/Research/SDG Corpus/")