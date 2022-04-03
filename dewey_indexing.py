from dendrogram_utils import createNodesList


def dewey_indexing(nodesList, rootNodeNumber, root_id="0", doc_id_index = {}, cluster_topic_index={}):
    """
    Generates the cluster index (dewey numbering)
    Args:
        - df: input dataframe of tf-idf vectors
        - model: clustering output
    Returns:
        - cluster index table
    """
    current_node = nodesList[rootNodeNumber]
    children = []
    if current_node["left"] is not None and current_node["right"] is not None:
        children = [current_node["left"], current_node["right"]]

    # cluster_topic_index[root_id] = dendrogram_root.topic

    if not len(children) == 0:
        higher_child_id = root_id + ".0"
        lower_child_id = root_id + ".1"

        # if children[0].distance > children[1].distance:
        #     higher_child = children[0]
        #     lower_child=children[1]
        # else:
        #     higher_child = children[1]
        #     lower_child = children[0]
        higher_child = children[1]  # right child
        lower_child = children[0]  # left child

        dewey_indexing(nodesList, higher_child, higher_child_id, doc_id_index, cluster_topic_index)
        dewey_indexing(nodesList, lower_child, lower_child_id, doc_id_index, cluster_topic_index)
    else:
        doc_id_index[root_id]=rootNodeNumber

    return doc_id_index, cluster_topic_index
