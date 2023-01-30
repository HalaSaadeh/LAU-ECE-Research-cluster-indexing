import timeit

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from src.database_utils import load_table_to_dict

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
    start = timeit.default_timer()
    clusters = load_table_to_dict("dewey_db1.db", "cluster_topic_index")
    intra_similarity = average_intra_cluster_similarity(clusters)
    inter_similarity = average_inter_cluster_similarity(clusters)
    stop = timeit.default_timer()
    cluster_eval_time = stop - start
    print("Cluster Evaluation Time: ", cluster_eval_time)
    print("Intra cluster similarity: ", intra_similarity)
    print("Inter cluster similarity: ", inter_similarity)
