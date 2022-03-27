from sklearn.cluster import AgglomerativeClustering
from dendrogram_utils import get_basic_components, plot_dendrogram


def agglomorativeClustering(df, list_FeatureKeys):
    """
    Performs hierarchical clustering of text tf-idf vectors

    Args:
        - df: input dataframe of tf-idf vectors
    Returns:
        - stemmed text
    """
    hc1 = AgglomerativeClustering(distance_threshold=0, n_clusters=None, affinity='cosine', linkage='average')
    y_hc1 = hc1.fit(df)

    plot_dendrogram(model=y_hc1)
    #
    # components = get_basic_components(hc1, len(df))
    # # centers = get_dend_centers(B)
    #
    # DS = dendrogramDS(df, components)
    # print(DS)
    # return (DS, list_FeatureKeys)