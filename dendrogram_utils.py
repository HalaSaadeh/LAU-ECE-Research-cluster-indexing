import numpy as np
from scipy.cluster.hierarchy import dendrogram
from matplotlib import pyplot as plt


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


def get_basic_components(model, NB_ELEMENTS):
    temp_dict = {}
    cluster_combinations = model.children_

    to_return = []
    MAX_INDEX = NB_ELEMENTS - 1
    count = NB_ELEMENTS

    # corner case: more than 2 in the same cluster
    for i in range(len(cluster_combinations)):
        temp = []
        for j in range(2):
            x = cluster_combinations[i][j]
            if x <= MAX_INDEX:
                temp.append(x)
            else:
                a = grab_deep_elements(x, temp_dict, MAX_INDEX)
                for el in a:
                    temp.append(el)
        temp_dict[count] = temp
        count += 1
        to_return.append(temp)

    return to_return


def grab_deep_elements(x, dict, MAX_INDEX):
    lista = dict.get(x)
    returned_list = []

    for el in lista:
        if el <= MAX_INDEX:
            returned_list.append(el)
        else:
            grab_deep_elements(el, dict, MAX_INDEX)

    return returned_list


def get_dend_centers(d):
    '''takes a scipy.dendrogram as an input'''
    dend_centers = []
    for ycoords, xcoords in zip(d['icoord'], d['dcoord']):
        #   To get the center: x= f (or g), y = (a+b)/2
        xcenter = xcoords[1]
        ycenter = (ycoords[2] + ycoords[1]) / 2
        dend_centers.append((xcenter, ycenter))
    dend_centers.sort(key= lambda x:x[0])
    #print('Dendrogram centers: ', dend_centers)
    return dend_centers


# I can add the parent to make it like the DDL
class Node:
    def __init__(self, leftNode, rightNode, featureVector, deepNodes):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.deepNodes = deepNodes
        # self.distance = distance

        if (self.leftNode != None and self.rightNode != None):
            self.featureVector = list(map(add, self.leftNode.featureVector, self.rightNode.featureVector))
        else:
            self.featureVector = featureVector

    def __repr__(self):
        # return "DeepNodes:" +  ','.join(str(v) for v in self.deepNodes)+"\nDistance:" + str(self.distance)+"\nFeatureVector:"+ str(list(self.featureVector))
        return "DeepNodes:" + ','.join(str(v) for v in self.deepNodes)
        # return "DeepNodes:" +  ','.join(str(v) for v in self.deepNodes) +"\tFeatureVector:"+ str(list(self.featureVector))

    def __str__(self):
        # return "DeepNodes:" +  ','.join(str(v) for v in self.deepNodes)+"\nDistance:" + str(self.distance)+"\nFeatureVector:"+ str(list(self.featureVector))
        return "DeepNodes:" + ','.join(str(v) for v in self.deepNodes)
        # return "DeepNodes:" +  ','.join(str(v) for v in self.deepNodes) + "\tFeatureVector:"+ str(list(self.featureVector))


class dendrogramDS:
    def __init__(self, df, basicComponents):
        self.allNodesBySize = {"1": []}
        self.nodeSizes = [1]
        self.rootNode = None
        for i in range(df.shape[0]):
            self.allNodesBySize["1"].append(Node(None, None, list(df.iloc[i]), [i]))
        for i, bcomponent in enumerate(basicComponents):
            componentLength = len(bcomponent)
            if (componentLength not in self.nodeSizes):
                self.nodeSizes.append(componentLength)
                self.nodeSizes.sort()  # I dont think we need this but just to make sure

            if (componentLength == 2):
                try:
                    self.allNodesBySize["2"].append(Node(self.allNodesBySize["1"][bcomponent[0]],
                                                         self.allNodesBySize["1"][bcomponent[1]], None,
                                                         bcomponent
                                                         ))
                except:
                    self.allNodesBySize["2"] = [Node(self.allNodesBySize["1"][bcomponent[0]],
                                                     self.allNodesBySize["1"][bcomponent[1]], None,
                                                     bcomponent
                                                     )]
            else:
                startLookingFromSize_Index = self.nodeSizes.index(componentLength) - 1
                nbComponentToCheck = componentLength
                temp_leftNode = None
                temp_rightNode = None
                found_left = False
                found_right = False

                while (nbComponentToCheck != 0):
                    found = False
                    for j in self.allNodesBySize[str(self.nodeSizes[startLookingFromSize_Index])]:
                        if (nbComponentToCheck < self.nodeSizes[startLookingFromSize_Index]):
                            break
                        try:
                            temp = bcomponent.index(j.deepNodes[0])
                            if (temp == 0 and not found_left):
                                temp_leftNode = j
                                found_left = True
                                found = True
                                nbComponentToCheck -= len(j.deepNodes)

                            elif (temp != 0 and not found_right):
                                if (temp + len(j.deepNodes) >= componentLength):
                                    temp_rightNode = j
                                    found_right = True
                                    found = True
                                    nbComponentToCheck -= len(j.deepNodes)

                            else:
                                continue
                        except:
                            continue

                    if (not found):
                        startLookingFromSize_Index -= 1
                    else:
                        if (nbComponentToCheck != 0):
                            startLookingFromSize_Index = self.nodeSizes.index(nbComponentToCheck)
                            found = False

                if (temp_leftNode == None and temp_rightNode == None):
                    print("ERROR")

                else:
                    try:
                        self.allNodesBySize[str(componentLength)].append(Node(temp_leftNode,
                                                                              temp_rightNode,
                                                                              None,
                                                                              bcomponent
                                                                              ))
                    except:
                        self.allNodesBySize[str(componentLength)] = [Node(temp_leftNode,
                                                                          temp_rightNode,
                                                                          None,
                                                                          bcomponent
                                                                          )]

        self.rootNode = self.allNodesBySize[str(df.shape[0])][0]