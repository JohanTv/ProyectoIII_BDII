from rtree import index
import face_recognition
import pickle
import pandas as pd
from datetime import datetime 
import numpy as np
import os
from queue import PriorityQueue

scaler_path = "./bin/scaler.dat"
pca_path = "./bin/pca.dat"
ncomponents_path = "./bin/ncomponents.dat"

scaler = pickle.load(open(scaler_path, "rb"))
pca = pickle.load(open(pca_path, "rb"))
ncomponents = pickle.load(open(ncomponents_path, "rb"))

idx = None
collection = None
y = None

def initialize_rtree(path_rtree = "./bin/rtree_index"):
    global idx
    p = index.Property()
    p.dimension = ncomponents #D
    idx = index.Index(path_rtree, properties=p)

def initiliaze_df(path):
    global collection, y
    df_path = "./data/datasetv2.csv"
    #df_path = path
    df = pd.read_csv(df_path)
    features = [str(i) for i in range(1, ncomponents+1)]
    collection = df.loc[:, features]
    y = df.loc[:, ["path"]]

def generate_df(x):
    return pd.DataFrame(data=x, columns = [str(i) for i in range(1, 129)])

def generate_point(v):
    return tuple(np.concatenate([v, v], axis = None))

def ED(v1, v2):
    return np.linalg.norm(v1-v2)

def parser_image(image_path):
    picture = face_recognition.load_image_file(image_path)    
    all_face_encodings = face_recognition.face_encodings(picture)
    x = generate_df(all_face_encodings)
    x_scaled = scaler.transform(x)
    x_pca = pca.transform(x_scaled)
    return x_pca[0]

def range_seach(image_path, radio):
    initiliaze_df()
    query = parser_image(image_path)
    result = []
    nrows = collection.shape[0]
    for i in range(nrows):
        dist = ED(collection.iloc[i].values, query)
        if(dist < radio):
            image_path = y.iloc[i].values[0]
            result.append(image_path)
    return result

def knearest(image_path, k, path_r_tree):
    initialize_rtree(path_r_tree)
    x_pca = parser_image(image_path)
    point = generate_point(x_pca)
    result = list(idx.nearest(coordinates=point, num_results=k, objects="raw"))
    return result

def searchKNN_sequential(image_path, k, path):
    initiliaze_df(path)
    query = parser_image(image_path)
    pq = PriorityQueue()
    nrows = collection.shape[0]
    for i in range(nrows):
        dist = ED(collection.iloc[i].values, query) * (-1)
        image_path = y.iloc[i].values[0]
        if(pq.qsize() < k):
            pq.put((dist, image_path))
        else:
            top = pq.get()
            if(dist > top[0]):
                pq.put((dist, image_path))
            else:
                pq.put(top)
    result = [0] * k
    i = k - 1
    while not pq.empty():
        data = pq.get()
        result[i] = data[1]
        i -= 1
    return result

def parser(prev_result):
    result = '{'
    count = 1
    for elem in prev_result:
        if count != len(prev_result):
            result += '{"url": '+'"'+elem+'"'+'},'
        else:
            result += '{"url": '+'"'+elem+'"'+'}'
        count += 1

    result += '}'

    return result


# image_path = "test/Roger_Moore_0004.jpg"
# #result = knearest(image_path, 8)
# #result = searchKNN_sequential(image_path, 8)
# start_time = datetime.now() 
# #result = range_seach(image_path, 10) # radio -> [9, 11] recomendable
# result = knearest(image_path, 8)
# time_elapsed = datetime.now() - start_time 
# #print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
# start_time = datetime.now() 
# result = searchKNN_sequential(image_path, 8)
# #result = range_seach(image_path, 10) # radio -> [9, 11] recomendable
# time_elapsed = datetime.now() - start_time 
# #print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
# # os.remove('bin_test/rtree_index.dat')
# # os.remove('bin_test/rtree_index.idx')
# jsonResult = parser(result)
# print(jsonResult)