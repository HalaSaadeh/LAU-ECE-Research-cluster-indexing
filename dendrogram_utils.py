import numpy as np
from scipy.cluster.hierarchy import dendrogram
from matplotlib import pyplot as plt
import dendrogram_utils as du
import itertools


def plot_dendrogram(model, **kwargs):
    """
    Plots the dendrogram. Code snippet is taken from scikit-learn.org
    """
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_, counts]).astype(float)

    # Plot the corresponding dendrogram
    plt.title("Hierarchical Clustering Dendrogram")
    dendrogram(linkage_matrix, **kwargs)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plt.show()

class Node:
    def __init__(self, nodeNumber, leftNode=None, rightNode=None, featureVector=None):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.nodeNumber = str(nodeNumber)

    def __str__(self):
        return "Node Number:" + str(self.nodeNumber) + ". Left node: " + str(self.leftNode) + ". Right node: " + \
               str(self.rightNode)

    def __repr__(self):
        return "Node Number:" + str(self.nodeNumber) + ". Left node: " + str(self.leftNode) + ". Right node: " + \
               str(self.rightNode)


def createNodesList(df, model, filenames):
    """
        Returns list of nodes with their corresponding left and right child
        Args:
            - df: input data frame
            - model: model after fitting during clustering
        Returns:
            - nodeDict: dictionary of nodes and their children
    """
    # Create list of leaf/document nodes
    numberOfDocuments = df.shape[0]
    documentNodes = []
    for i in range(numberOfDocuments):
        node = {i: {"left":None, "right": None, "doc": filenames[i]}}
        documentNodes.append(node)

    # Create list of cluster nodes
    ii = itertools.count(df.shape[0])
    clusterNodes = [{next(ii): {'left': x[0], 'right': x[1]}} for x in model.children_]
    # clusterNodes= [du.Node(nodeNumber=next(ii), leftNode=x[0], rightNode=x[1]) for x in model.children_]

    # Combine the two lists into a list of nodes
    nodeList = documentNodes + clusterNodes

    # Convert the list of nodes to an accessible dict
    nodeDict = {}
    for node in nodeList:
        nodeDict.update(node)

    # Get rootNodeNumber
    rootNodeNumber = getRootNodeNumberFromNodeList(nodeDict)
    print(nodeDict)
    return nodeDict, rootNodeNumber


def getRootNodeNumberFromNodeList(nodeList: dict):
    """
        Returns the node number of the root note
        Args:
            - nodeList: input dict of nodes
        Returns:
            - bool true or false
    """
    nodeIds = nodeList.keys()
    rootNodeNumber = max(nodeIds)
    return rootNodeNumber
