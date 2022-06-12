# LAU ECE Research: Cluster Indexing
Source code implementation for the indexing component of the "Hierarchical Indexing for Interactive Zooming of Document Clusters" research study.  
This study was performed at the Lebanese American University in the Electrical and Computer Engineering (ECE) department. 

## Description
### Overall System Architecture
The overall architecture of the system can be found below:  
![alt text](https://github.com/HalaSaadeh/LAU-ECE-Research-cluster-indexing/blob/main/readme_images/overall_architecture.png "Overall Architecture")

This repository contains the source code for the *Indexing (offline) component.*
The repository for the **Visualization component** can be found here: [LAU-ECE-Research-cluster-visualization](https://github.com/HalaSaadeh/LAU-ECE-Research-cluster-visualization) 
## Indexing Component
This code contains the **Indexing Component** of the project. This component receives a document collection as input and produces a hierarchical index structure as output after performing the following steps:  
- Document Preprocessing
- Document clustering
- Topic extraction
- Document cluster indexing

The output index will be stored in an SQLite database file. The output index will be found in **src/dewey_db.db**.  

## Experimental Results
Performance experiments were conducted to measure the following metrics: 
- **Index building time:** the time taken to preprocess, cluster, extract the topics, and build the index structure, while varying the size of the dataset.
- **Index size in-memory:** the size of the index tables stored in-memory, while varying the size of the dataset.
The experiment results can be found in **Indexing_results.xlsx**.

## Repository Structure  
The repository is structured as follows:  
- **readme_images**: source images for this README document
- **src**: implementation source code
- **Indexing_results.xlsx**: Experimental results and charts
- **requirements.txt**: Python dependencies list

## Dependencies 
Project dependencies can be found in **requirements.txt**. Run `pip install requirements.txt` to install all the required dependencies.

## Example
Consider the following example as a high level overview of this code repository.
### Input 
An example input is the following set of 10 documents. These documents represent 10 out of the 17 UN Sustainable Development Goals (SDGs).  
![alt text](https://github.com/HalaSaadeh/LAU-ECE-Research-cluster-indexing/blob/main/readme_images/document_list.png "Input document list")

### Preprocessing, Clustering, and Topic Extraction
The documents are preprocessed and then clustered. Then, the topic keywords are extracted for each cluster.  
The output dendrogram produced after clustering can be found below:  
![alt text](https://github.com/HalaSaadeh/LAU-ECE-Research-cluster-indexing/blob/main/readme_images/output_dendrogram.png "Output dendrogram")

### Indexing
The clusters and their associated topics are then used to produce the index.  
The dendrogram will be labeled as follows:  
![alt text](https://github.com/HalaSaadeh/LAU-ECE-Research-cluster-indexing/blob/main/readme_images/labelled_dendrogram.png "Labeled dendrogram")
The index tables produced can be viewed below:  
![alt text](https://github.com/HalaSaadeh/LAU-ECE-Research-cluster-indexing/blob/main/readme_images/output_index.png "Output index")
