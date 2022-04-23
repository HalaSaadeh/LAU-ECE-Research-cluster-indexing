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
    for i in range(dendrogram_height + 1):
        getLevel(nodesList, rootNodeNumber, i, level_order_list)
    level_order_numbers = {}
    for i in range(len(level_order_list)):
        level_order_numbers[level_order_list[i]] = i
    return level_order_numbers


def laf_indexing(nodesList, rootNodeNumber, levelOrderNumbersDict, level_order_number=0, father_number=-1,
                 level_number=0, doc_id_index={}, cluster_topic_index={}, laf_index={}):
    """
    Generates the cluster index (LAF numbering)
    """

    current_node = nodesList[rootNodeNumber]
    children = []
    if current_node["left"] is not None and current_node["right"] is not None:
        children = [current_node["left"], current_node["right"]]

    root_id = str(level_order_number) + "." + str(father_number) + "." + str(level_number)
    laf_index[level_order_number] = father_number #[father_number, level_number]
    cluster_topic_index[root_id] = current_node["topic"]

    if not len(children) == 0:
        left = current_node["left"]
        level_order_number_left = levelOrderNumbersDict[left]
        laf_indexing(nodesList, current_node["left"], levelOrderNumbersDict, level_order_number=level_order_number_left,
                     father_number=level_order_number, level_number=level_number + 1, doc_id_index=doc_id_index,
                     cluster_topic_index=cluster_topic_index, laf_index=laf_index)
        level_order_number_right = levelOrderNumbersDict[current_node["right"]]
        laf_indexing(nodesList, current_node["right"], levelOrderNumbersDict,
                     level_order_number=level_order_number_right,
                     father_number=level_order_number, level_number=level_number + 1, doc_id_index=doc_id_index,
                     cluster_topic_index=cluster_topic_index, laf_index=laf_index)
    else:
        doc_id_index[root_id] = nodesList[rootNodeNumber]["doc"]

    return doc_id_index, cluster_topic_index, laf_index
