import search
import time
import os
import pandas as pd
import pickle
import numpy as np
from rtree import index

def create_rtree(size):
    dataset_path = "./data/dataset_" + str(size) + ".csv"
    rtree_path = "./bin_test/rtree_index_" + str(size)
    df = pd.read_csv(dataset_path)
    ncomponents = pickle.load(open("./bin/ncomponents.dat", "rb"))
    nrows = df.shape[0]
    features = [str(i) for i in range(1, ncomponents+1)]
    x = df.loc[:, features]
    y = df.loc[:, ["path"]]
    p = index.Property()
    p.dimension = ncomponents
    idx = index.Index(rtree_path, properties = p)
    for i in range(nrows):
        v = x.iloc[i].values
        image = y.iloc[i].values[0]
        point = tuple(np.concatenate([v, v]))
        idx.insert(i, point, obj=image)
    idx.close()

def timeKnrearest(size):
    image_path = "test/Roger_Moore_0004.jpg"
    start = time.perf_counter()
    search.knearest(image_path, 8, "./bin_test/rtree_index_" + str(size))
    end = time.perf_counter()
    print(f"Knearest with size: {size} elements finished in {end - start:0.4f} seconds")


def timeSequentialKnn(size):
    string = "./data/dataset_" + str(size) + ".csv"
    image_path = "test/Roger_Moore_0004.jpg"
    start = time.perf_counter()
    search.searchKNN_sequential(image_path, 8, string)
    end = time.perf_counter()
    print(f"Sequential Knn with size: {size} elements finished in {end - start:0.4f} seconds")


sizes = [100, 200, 400, 800, 1600, 3200, 6400, 12800]
search.initialize_models("./bin/scaler.dat", "./bin/pca.dat", "./bin/ncomponents.dat")
for size in sizes:
    create_rtree(size)
    timeKnrearest(size)
    timeSequentialKnn(size)
