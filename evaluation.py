import timeit
from pympler import asizeof
from main import pre_indexing, indexing_dewey, indexing_laf


datasets = [
    # ("Resolutions Ecosoc Eng 2021", "D:\Research\Resolutions Corpus\Res\EcoSoc\Eng 2021", 5),
    ("SDG Corpus", "D:/Research/SDG Corpus/", 15),
    # ("SDG Corpus", "D:/Research/SDG 15", 15),
    # ("SDG Corpus Dup", "D:/Research/SDG 30", 30),
    # ("SDG Full Dataset", "D:/Research/SDG 45",  45),
    # ("SDG Full Dataset", "D:/Research/SDG Full Dataset 60", 60),
    # ("SDG Full Dataset", "D:/Research/SDG FullDataset - Copy/FullDataset", 120),
    # ("SDG Full Dataset", "D:/Research/SDG FullDataset Mod/FullDataset", 180),
    # ("SDG Full Dataset", "D:/Research/SDG FullDataset Mod - Copy/FullDataset", 240),
    # ("SDG Full Dataset", "D:/Research/SDG FullDataset Mod - Copy - Copy/FullDataset", 300)

]

for dataset in datasets:

    # nodesList, rootNumber = pre_indexing(dataset)

    doc_id_index, cluster_topic_index = indexing_dewey(dataset)
    print(doc_id_index)


    # start = timeit.default_timer()
    # doc_id_index, cluster_topic_index, laf_index = indexing_laf(nodesList, rootNumber)
    # stop = timeit.default_timer()
    # laf_build_time = stop - start
    # total_index_size_laf = (asizeof.asizeof(doc_id_index) + asizeof.asizeof(cluster_topic_index) +
    #                         asizeof.asizeof(laf_index))/(1024*1024)
    # csv_row = [dataset[0], dataset[2], dewey_build_time, total_index_size_dewey, laf_build_time,total_index_size_laf]
    # writer.writerow(csv_row)

# f.close()
