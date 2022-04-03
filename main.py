from file_utils import extractDataset
from text_utils import textToDataFrame
from hierarchical_clustering import agglomorativeClustering
from dendrogram_utils import createNodesList
from dewey_indexing import dewey_indexing


# Extract dataset
content = extractDataset("D:/Research/SDG Corpus/")
# content = extractDataset("D:/Research/Resolutions Corpus/Res/EcoSoc/Eng 2020/")

# Convert text to tf-idf vectors
content_df, content_featurekeys = textToDataFrame(content)

# Compute clustering
model, list_FeatureKeys = agglomorativeClustering(content_df, content_featurekeys)

# Get list of cluster nodes
nodesList, rootNodeNumber = createNodesList(content_df, model)

# Generate the indexes (Dewey numbering)
doc_id_index, cluster_topic_index = dewey_indexing(nodesList, rootNodeNumber)
print(doc_id_index)