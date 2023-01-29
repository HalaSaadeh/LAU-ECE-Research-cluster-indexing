import sqlite3
import ast
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def load_table_to_dict(db_file: str, table_name: str):
    """
    This function loads the entire table from an SQLite database into a Python dict.

    Args:
    - db_file (str): The path to the SQLite database file.
    - table_name (str): The name of the table to be loaded.

    Returns:
    - data_dict (dict): A dictionary where the key is the 'id' and the value is the 'topic'
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Retrieve data from the table
    c.execute("SELECT * FROM {}".format(table_name))
    rows = c.fetchall()

    # Create a dictionary from the data
    data_dict = {row[0]: ast.literal_eval(row[1]) for row in rows}

    # Close the connection to the database
    conn.close()

    return data_dict


def average_intra_cluster_similarity(clusters: dict) -> float:
    """
    Compute the average intra-cluster similarity for a given set of hierarchical clusters.
    :param clusters: A dictionary where the keys are cluster IDs (strings) and the values are lists of strings representing the topics of the clusters.
    :return: The average intra-cluster similarity (float)
    """
    similarities = []
    for cluster_id, cluster_topic in clusters.items():
        child_clusters = [clusters[child_cluster_id] for child_cluster_id in clusters.keys() if
                          child_cluster_id.startswith(cluster_id + '.')]
        if child_clusters:
            for child_cluster_topic in child_clusters:
                # similarity = cosine_similarity(np.array([cluster_topic]).reshape(1, -1),
                #                                np.array([child_cluster_topic]).reshape(1, -1))[0][0]
                # Convert lists to numerical representation
                vectorizer = CountVectorizer()
                cluster_vector = vectorizer.fit_transform([' '.join(cluster_topic)])
                child_cluster_vector = vectorizer.transform([' '.join(child_cluster_topic)])

                # Compute cosine similarity
                similarity = cosine_similarity(cluster_vector, child_cluster_vector)[0][0]
                similarities.append(similarity)
    return np.mean(similarities)


def average_inter_cluster_similarity(clusters: dict) -> float:
    """
    Compute the average inter-cluster similarity for a given set of hierarchical clusters.
    :param clusters: A dictionary where the keys are cluster IDs (strings) and the values are lists of strings representing the topics of the clusters.
    :return: The average inter-cluster similarity (float)
    """
    similarities = []
    for cluster_id, cluster_topic in clusters.items():
        for other_cluster_id, other_cluster_topic in clusters.items():
            if other_cluster_id != cluster_id:
                # Convert lists to numerical representation
                vectorizer = CountVectorizer()
                cluster_vector = vectorizer.fit_transform([' '.join(cluster_topic)])
                other_cluster_vector = vectorizer.transform([' '.join(other_cluster_topic)])

                # Compute cosine similarity
                similarity = cosine_similarity(cluster_vector, other_cluster_vector)[0][0]
                similarities.append(similarity)
    return np.mean(similarities)

if __name__ == "__main__":
    clusters = load_table_to_dict("dewey_db.db", "cluster_topic_index")
    intra_similarity = average_intra_cluster_similarity(clusters)
    inter_similarity = average_inter_cluster_similarity(clusters)
    print("Intra cluster similarity: ", intra_similarity)
    print("Inter cluster similarity: ", inter_similarity)
