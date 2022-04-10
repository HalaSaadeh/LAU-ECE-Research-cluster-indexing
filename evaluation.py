import timeit
from pympler import asizeof
from main import pre_indexing, indexing_dewey, indexing_laf
import csv

f = open('D:/Research/Implementation/undergrad-research-indexing/results.csv', 'w')

# create the csv writer
writer = csv.writer(f)

csv_header = ["Dataset", "# Documents", "Dewey IndexBuild Time", "Dewey Index Build Size",
              "LAF IndexBuild Time", "LAF Index Build Size"]
writer.writerow(csv_header)

datasets = [
    ("Resolutions Ecosoc Eng 2021", "D:\Research\Resolutions Corpus\Res\EcoSoc\Eng 2021", 5),
    ("SDG Corpus", "D:/Research/SDG Corpus/", 15),
    ("Resolutions Ecosoc Eng 2020", "D:/Research/Resolutions Corpus/Res/EcoSoc/Eng 2020/", 32),
    ("Resolutions Escwa Since 2006", "D:/Research/Resolutions Corpus/Res/ESCWA Res (since 2006)", 69),

]

for dataset in datasets:

    nodesList, rootNumber = pre_indexing(dataset[1])

    start = timeit.default_timer()
    doc_id_index, cluster_topic_index = indexing_dewey(nodesList, rootNumber)
    stop = timeit.default_timer()
    dewey_build_time = stop - start
    total_index_size_dewey = (asizeof.asizeof(doc_id_index) + asizeof.asizeof(cluster_topic_index))/(1024*1024)

    start = timeit.default_timer()
    doc_id_index, cluster_topic_index, laf_index = indexing_laf(nodesList, rootNumber)
    stop = timeit.default_timer()
    laf_build_time = stop - start
    total_index_size_laf = (asizeof.asizeof(doc_id_index) + asizeof.asizeof(cluster_topic_index) +
                            asizeof.asizeof(laf_index))/(1024*1024)
    csv_row = [dataset[0], dataset[2], dewey_build_time, total_index_size_dewey, laf_build_time,total_index_size_laf]
    writer.writerow(csv_row)

f.close()
