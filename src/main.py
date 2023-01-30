import timeit

from pympler import asizeof

from src.file_utils import extractDataset
from src.text_utils import textToDataFrame
from src.hierarchical_clustering import agglomorativeClustering
from src.dendrogram_utils import createNodesList
from src.dewey_indexing import dewey_indexing
from src.sqlite_utils import insert_index_as_table
from src.topic_extraction import getClusterVectors, getTopKKeywordsForEachCluster, appendKeywordListToNodeList
import csv

f = open('D:/Research/Implementation/undergrad-research-indexing/results.csv', 'w')

# create the csv writer
writer = csv.writer(f)

csv_header = ["# Documents", "Doc Preprocessing Time", "Hierarchical Clustering Time",
              "Topic Extraction Time", "Indexing Time", "Document Index Size", "Topic Index Size"]
writer.writerow(csv_header)


def pre_indexing(datasetPath):
    start = timeit.default_timer()
    # Extract dataset
    filenames, content = extractDataset(datasetPath[1])
    num_docs = datasetPath[2]

    # Convert text to tf-idf vectors
    content_df, content_featurekeys = textToDataFrame(content)
    stop = timeit.default_timer()
    preprocessing_time = stop - start

    # Compute clustering
    start = timeit.default_timer()
    model, list_FeatureKeys = agglomorativeClustering(content_df, content_featurekeys)

    # Get list of cluster nodes
    nodesList, rootNodeNumber = createNodesList(content_df, model, filenames)
    stop = timeit.default_timer()
    clustering_time = stop - start

    start = timeit.default_timer()
    # Get top K keywords from each cluster and add the information to the nodesList
    new_df = getClusterVectors(df=content_df, nodeList=nodesList, nodeListRootNumber=rootNodeNumber)
    topKkeys = getTopKKeywordsForEachCluster(new_df, 6)
    nodeList_withTopics = appendKeywordListToNodeList(nodesList, topKkeys)
    stop = timeit.default_timer()
    topic_time = stop - start

    results = {"num_docs": num_docs, "preprocessing": preprocessing_time, "clustering": clustering_time, "topic_extraction": topic_time}

    return nodesList, rootNodeNumber, results


def indexing_dewey(dataset, i):
    nodesList, rootNodeNumber, results = pre_indexing(dataset)

    start = timeit.default_timer()
    # Generate the indexes (Dewey numbering)
    doc_id_index, cluster_topic_index = dewey_indexing(nodesList, rootNodeNumber, "0", {}, {})

    # Insert the indices to the SQL table
    DEWEY_DB_PATH = "D:/Research/Implementation/undergrad-research-indexing/src/dewey_db" + str(i) + ".db"
    insert_index_as_table(DEWEY_DB_PATH, "doc_table_index", doc_id_index)
    insert_index_as_table(DEWEY_DB_PATH, "cluster_topic_index", cluster_topic_index)
    stop = timeit.default_timer()
    indexing_time = stop - start

    doc_index_size = asizeof.asizeof(doc_id_index)/(1024*1024)
    topic_index_size = asizeof.asizeof(cluster_topic_index)/(1024*1024)


    csv_row = [results["num_docs"], results["preprocessing"], results["clustering"], results["topic_extraction"], indexing_time, doc_index_size, topic_index_size]
    writer.writerow(csv_row)

    return doc_id_index, cluster_topic_index
