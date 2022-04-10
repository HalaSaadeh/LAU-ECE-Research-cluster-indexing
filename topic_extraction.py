from operator import add
import pandas as pd
import numpy as np


def getClusterVectors(df, nodeList, nodeListRootNumber):
    """
        Takes data frame of documents and their tf-idf vectors and returns the same dataframe with the vectors for each
        document cluster appended as well.
        Args:
            - df: input data frame of TF-IDF vectors for all input documents
            - nodeList: input dict of nodes
            - nodeListRootNumber: root number of input dict of nodes (highest cluster)
        Returns:
            - df: output data frame of TF-IDF vectors for all input documents as well as clusters
    """

    if nodeList[nodeListRootNumber]["left"] is None or nodeList[nodeListRootNumber]["right"] is None:
        return df
    left_child = nodeList[nodeListRootNumber]["left"]
    right_child = nodeList[nodeListRootNumber]["right"]
    df = getClusterVectors(df, nodeList, left_child)
    df = getClusterVectors(df, nodeList, right_child)
    new_df_row = df.loc[left_child] + df.loc[right_child]
    new_df_row.name = nodeListRootNumber
    df = df.append([new_df_row])
    return df


def getTopKKeywordsForEachCluster(df, k):
    """
    Extracts top K keywords for each cluster in df.
    Args:
        - df: input data frame of TF-IDF vectors for all input documents and clusters
        - k: number of keywords to extract
    Returns:
        - result: data frame with top K keywords for each document / cluster
    """
    column_names = range(1,k+1)
    result = pd.DataFrame(np.zeros((0, k)), columns=column_names)
    df_transposed = df.T
    for i in df_transposed.columns:
        df1row = pd.DataFrame(df_transposed.nlargest(k, i).index.tolist(), index=column_names).T
        result = pd.concat([result, df1row], axis=0)
    result = result.reset_index(drop=True)
    return result

