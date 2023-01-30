import csv
import os
import shutil
import timeit

from src.cluster_quality_evaluations import average_inter_cluster_similarity, average_intra_cluster_similarity
from src.database_utils import load_table_to_dict
from src.main import indexing_dewey


def insert_document_heuristic():
    existing_clusters = load_table_to_dict("dewey_db.db", "cluster_topic_index")


def insert_document_repeat_clustering(doc_path, new_path_append):
    # original_dataset = ("SDG Full Dataset", "D:/Research/SDG/1000", 1000)
    original_dataset = ("SDG Full Dataset", "D:/Research/SDG/1000", 1000)
    # original_dataset = ("SDG Full Dataset", "D:/Research/SDG/100", 100)
    # specify the original path
    original_path = original_dataset[1]

    # specify the new path
    new_path = original_path + str(new_path_append)
    new_dataset = ("New directory", new_path, original_dataset[2]+1)

    # create the new path if it doesn't exist
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    # copy all files from original path to new path
    for filename in os.listdir(original_path):
        shutil.copy(os.path.join(original_path, filename), os.path.join(new_path, filename))

    # copy the document to the new directory
    shutil.copy(doc_path, new_path)

    indexing_dewey(new_dataset, new_path_append)



def index_update_experiments(new_doc_paths = "D:/Research/DocsToAdd"):
    filenames = []
    for filename in os.listdir(new_doc_paths):
        filenames.append(os.path.join(new_doc_paths, filename))

    for i in range(11):
        start = timeit.default_timer()
        for j in range(i):
            insert_document_repeat_clustering(filenames[j], i)
        stop = timeit.default_timer()
        index_update_time = stop - start

        csv_row = [i, index_update_time]
        writer.writerow(csv_row)


if __name__=="__main__":
    # insert_document_repeat_clustering("D:/Research/SDG FullDataset/FullDataset/b e_escwa_sdpd_15_1_e.pdf")

    f = open('D:/Research/Implementation/undergrad-research-indexing/index-update-results.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)

    csv_header = ["# Documents Inserted", "Index Update Time", "Cluster Evaluation Time",
                  "Inter-Cluster Similarity", "Intra-Cluster Similarity"]
    writer.writerow(csv_header)

    index_update_experiments()
