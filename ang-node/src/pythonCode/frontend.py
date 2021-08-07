import search
import os
import sys
import json

search.scaler_path = "./src/pythonCode/bin/scaler.dat"
search.pca_path = "./src/pythonCode/bin/pca.dat"
search.ncomponents_path = "./src/pythonCode/bin/ncomponents.dat"

search.initialize_models("./src/pythonCode/bin/scaler.dat", \
    "./src/pythonCode/bin/pca.dat", "./src/pythonCode/bin/ncomponents.dat")

#print("python: " + str(sys.argv[1]))
str_input = search.transform(str(sys.argv[1]))
image_path = "./src/pythonCode/images/"+ str_input + "/" + str_input + "_0001.jpg" #./imagen/obama/obama_0001.jpg
result = search.knearest(image_path, 8, "./src/pythonCode/bin/rtree_index")
jsonResult = search.parser(result)
with open('./src/pythonCode/result_db.json', 'w') as file:
    json.dump(jsonResult, file)