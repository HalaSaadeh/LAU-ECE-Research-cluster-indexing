from file_utils import extractDataset
from text_utils import textToDataFrame
from hierarchical_clustering import agglomorativeClustering

content = extractDataset("D:/Research/SDG Corpus/")
content_df, content_featurekeys = textToDataFrame(content)
agglomorativeClustering(content_df, content_featurekeys)