def getDendrogramHeight(nodeList, rootNode):
    """

    """
    left_child = nodeList[rootNode]["left"]
    right_child = nodeList[rootNode]["right"]
    if left_child is None and right_child is None:
        return 1
    left_height = getDendrogramHeight(nodeList, left_child)
    right_height = getDendrogramHeight(nodeList, right_child)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


def getLevel(nodeList, rootNode, level, level_order_number =0):
    if rootNode is None:
        return

    left_child = nodeList[rootNode]["left"]
    right_child = nodeList[rootNode]["right"]
    if level == 1:
        print(rootNode, nodeList[rootNode])
    elif level > 1:
        getLevel(nodeList, left_child, level - 1)
        getLevel(nodeList, right_child, level - 1)



def laf_indexing(nodesList, rootNodeNumber, level_order_number="0", level_number = 0, doc_id_index = {}, cluster_topic_index={}):
    """
    Generates the cluster index (LAF numbering)
    Args:
        - df: input dataframe of tf-idf vectors
        - model: clustering output
    Returns:
        - cluster index table
    """
    dendrogram_height = getDendrogramHeight(nodesList, rootNodeNumber)
    for i in range(dendrogram_height):
        getLevel(nodesList, rootNodeNumber, i)