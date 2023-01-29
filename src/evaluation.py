from src.main import indexing_dewey

datasets = [
    # ("SDG Corpus", "D:/Research/SDG Corpus 10/", 10),
    # ("SDG Corpus", "D:/Research/SDG 15", 15),
    # ("SDG Corpus Dup", "D:/Research/SDG 30", 30),
    # ("SDG Full Dataset", "D:/Research/SDG 45",  45),
    ("SDG Full Dataset", "D:/Research/SDG Full Dataset 60", 60),
    # ("SDG Full Dataset", "D:/Research/SDG FullDataset - Copy/FullDataset", 120),
    # ("SDG Full Dataset", "D:/Research/SDG FullDataset Mod/FullDataset", 180),
    # ("SDG Full Dataset", "D:/Research/SDG FullDataset Mod - Copy/FullDataset", 240),
    # ("SDG Full Dataset", "D:/Research/SDG FullDataset Mod - Copy - Copy/FullDataset", 300)
    # ("SDG Full Dataset", "D:/Research/SDG/100", 100),70
    # ("SDG Full Dataset", "D:/Research/SDG/200", 200),
    # ("SDG Full Dataset", "D:/Research/SDG/300", 300),
    # ("SDG Full Dataset", "D:/Research/SDG/400", 400),
    # ("SDG Full Dataset", "D:/Research/SDG/500", 500),
    # ("SDG Full Dataset", "D:/Research/SDG/600", 600),
    # ("SDG Full Dataset", "D:/Research/SDG/700", 700),
    # ("SDG Full Dataset", "D:/Research/SDG/800", 800),
    # ("SDG Full Dataset", "D:/Research/SDG/900", 900),
    # ("SDG Full Dataset", "D:/Research/SDG/1000", 1000),

]

for dataset in datasets:

    doc_id_index, cluster_topic_index = indexing_dewey(dataset)
    print(doc_id_index)
