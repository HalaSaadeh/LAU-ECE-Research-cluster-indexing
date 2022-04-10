import timeit

from main import pre_indexing, indexing_dewey, indexing_laf

datasets = [
    "D:/Research/Resolutions Corpus/Res/EcoSoc/Eng 2020/",
    "D:/Research/SDG Corpus/"
]

nodesList, rootNumber = pre_indexing(datasets[0])

start = timeit.default_timer()
indexing_laf(nodesList, rootNumber)
stop = timeit.default_timer()
print('LAF Index Building Time: ', stop - start)

start = timeit.default_timer()
indexing_dewey(nodesList, rootNumber)
stop = timeit.default_timer()
print('Dewey Index Building Time: ', stop - start)
