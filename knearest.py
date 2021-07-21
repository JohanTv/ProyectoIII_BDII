from rtree import index
import face_recognition
import pickle
import pandas as pd
import numpy as np

scaler_path = "./bin/scaler.dat"
pca_path = "./bin/pca.dat"
ncomponents_path = "./bin/ncomponents.dat"

scaler = pickle.load(open(scaler_path, "rb"))
pca = pickle.load(open(pca_path, "rb"))
ncomponents = pickle.load(open(ncomponents_path, "rb"))

path = "./bin/rtree_index"
p = index.Property()
p.dimension = ncomponents #D

idx = index.Index(path, properties=p)

def generate_df(x):
    return pd.DataFrame(data=x, columns = [str(i) for i in range(1, 129)])

def generate_point(v):
    return tuple(np.concatenate([v, v]))

def knearest(image_path, k):
    picture = face_recognition.load_image_file(image_path)    
    all_face_encodings = face_recognition.face_encodings(picture)
    x = generate_df(all_face_encodings)
    x_scaled = scaler.transform(x)
    x_pca = pca.transform(x_scaled)
    point = generate_point(x_pca[0])
    result = list(idx.nearest(coordinates=point, num_results=k, objects="raw"))
    return result

image_path = "test/Roger_Moore_0004.jpg"
result = knearest(image_path, 6)
print(result)