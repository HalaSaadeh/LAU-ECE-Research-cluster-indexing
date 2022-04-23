from sklearn.cluster import AgglomerativeClustering
from dendrogram_utils import plot_dendrogram


def agglomorativeClustering(df, list_FeatureKeys):
    """
    Performs hierarchical clustering of text tf-idf vectors

    Args:
        - df: input dataframe of tf-idf vectors
    Returns:
        - dendrogram hierarchy
    """
    hc1 = AgglomerativeClustering(distance_threshold=0, n_clusters=None, affinity='cosine', linkage='average')
    model = hc1.fit(df)

    plot_dendrogram(model=model)
    return model, list_FeatureKeys
