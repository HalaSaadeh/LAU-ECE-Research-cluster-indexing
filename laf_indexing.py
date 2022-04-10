def getDendrogramHeight(nodeList, rootNode):
    """
    Gets the dendrogram height (# of levels)
    Args:
        - nodeList: input dict of nodes
        - rootNode: root number of input dict of nodes (highest cluster)
    Returns:
        - height of the dendrogram
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


def getLevel(nodeList, rootNode, level, level_order_list):
    """
    Gets all the nodes in a specific level and appends them to a list
    Args:
        - nodeList: input dict of nodes
        - rootNode: root number of input dict of nodes (highest cluster)
    """
    if rootNode is None:
        return

    left_child = nodeList[rootNode]["left"]
    right_child = nodeList[rootNode]["right"]
    if level == 1:
        level_order_list.append(rootNode)
    elif level > 1:
        getLevel(nodeList, left_child, level - 1, level_order_list)
        getLevel(nodeList, right_child, level - 1, level_order_list)


def getLevelOrderNumbers(nodesList, rootNodeNumber):
    """
    Gets the level order numbers of all the ndoes
    Args:
        - nodeList: input dict of nodes
        - rootNode: root number of input dict of nodes (highest cluster)
    Returns:
        - level_order_numbers: dict of all nodes and their level number
    """

    dendrogram_height = getDendrogramHeight(nodesList, rootNodeNumber)
    level_order_list = []
    for i in range(dendrogram_height):
        getLevel(nodesList, rootNodeNumber, i, level_order_list)
    level_order_numbers = {}
    for i in range(len(level_order_list)):
        level_order_numbers[level_order_list[i]] = i
    print(level_order_numbers)



def laf_indexing(nodesList, rootNodeNumber, level_order_number="0", level_number=0, doc_id_index={},
                 cluster_topic_index={}):
    """
    Generates the cluster index (LAF numbering)
    Args:
        - df: input dataframe of tf-idf vectors
        - model: clustering output
    Returns:
        - cluster index table
    """
    getLevelOrderNumbers(nodesList, rootNodeNumber)
