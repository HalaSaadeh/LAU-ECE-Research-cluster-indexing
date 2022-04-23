from file_utils import extractDataset
from text_utils import textToDataFrame
from hierarchical_clustering import agglomorativeClustering
from dendrogram_utils import createNodesList
from dewey_indexing import dewey_indexing
from sqlite_utils import insert_index_as_table
from topic_extraction import getClusterVectors, getTopKKeywordsForEachCluster, appendKeywordListToNodeList
from laf_indexing import laf_indexing, getLevelOrderNumbers


def pre_indexing(datasetPath):
    # Extract dataset
    filenames, content = extractDataset(datasetPath)

    # Convert text to tf-idf vectors
    content_df, content_featurekeys = textToDataFrame(content)

    # Compute clustering
    model, list_FeatureKeys = agglomorativeClustering(content_df, content_featurekeys)

    # Get list of cluster nodes
    nodesList, rootNodeNumber = createNodesList(content_df, model, filenames)

    # Get top K keywords from each cluster and add the information to the nodesList
    new_df = getClusterVectors(df=content_df, nodeList=nodesList, nodeListRootNumber=rootNodeNumber)
    topKkeys = getTopKKeywordsForEachCluster(new_df, 6)
    nodeList_withTopics = appendKeywordListToNodeList(nodesList, topKkeys)
    return nodesList, rootNodeNumber


def indexing_dewey(nodesList, rootNodeNumber):
    # Generate the indexes (Dewey numbering)
    doc_id_index, cluster_topic_index = dewey_indexing(nodesList, rootNodeNumber)

    # Insert the indices to the SQL table
    DEWEY_DB_PATH = "D:/Research/Implementation/undergrad-research-indexing/dewey_db.db"
    insert_index_as_table(DEWEY_DB_PATH, "doc_table_index", doc_id_index)
    insert_index_as_table(DEWEY_DB_PATH, "cluster_topic_index", cluster_topic_index)

    return doc_id_index, cluster_topic_index


def indexing_laf(nodesList, rootNodeNumber):
    # Generate the indexes (LAF numbering)
    levelOrderNumbersDict = getLevelOrderNumbers(nodesList, rootNodeNumber)
    doc_id_index, cluster_topic_index, laf_index = laf_indexing(nodesList, rootNodeNumber, levelOrderNumbersDict)

    # Insert the indices to the SQL table
    LAF_DB_PATH = "D:/Research/Implementation/undergrad-research-indexing/laf_db.db"
    insert_index_as_table(LAF_DB_PATH, "doc_table_index", doc_id_index)
    insert_index_as_table(LAF_DB_PATH, "cluster_topic_index", cluster_topic_index)
    insert_index_as_table(LAF_DB_PATH, "laf_index", laf_index)

    return doc_id_index, cluster_topic_index, laf_index
