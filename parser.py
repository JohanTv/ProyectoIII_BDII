import os
import face_recognition
import csv
import numpy as np
import threading
import math

images_path = "./images/"
images_folders = os.listdir(images_path)
print("Cantidad de carpetas a procesar: " + str(len(images_folders)))
n = 1
csvfile = open("dataset.csv", 'w', encoding='UTF8', newline='')
writer = csv.writer(csvfile)
header = [i for i in range(1, 129)]
header.append("path")
writer.writerow(header)

lock = threading.Lock()
    
def processing(images_folders = []):
    global writer    
    for images_folder in images_folders:
        images = os.listdir(images_path + images_folder + '/')
        for image in images:
            image_path = images_path + images_folder + '/' + image
            picture = face_recognition.load_image_file(image_path)    
            all_face_encodings = face_recognition.face_encodings(picture)
            for face_encoding in all_face_encodings:
                path = images_folder + "/" + image
                row = np.append(face_encoding, path)
                lock.acquire()
                writer.writerow(row)
                lock.release()

def execute():
    nthreads = 10
    size = len(images_folders)
    step = math.ceil(size / nthreads)
    threads = []
    for i in range(nthreads):
        start = i * step
        end = min((i+1)*step, size)
        v = images_folders[start:end]
        thread = threading.Thread(target=processing, args=(v,))
        threads.append(thread)
    
    for i in range(nthreads):
        threads[i].start()
    
    for i in range(nthreads):
        threads[i].join()

execute()