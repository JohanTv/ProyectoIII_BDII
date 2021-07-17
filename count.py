import os


images_path = "./images/"
images_folders = os.listdir(images_path)
print("Cantidad de carpetas a procesar: " + str(len(images_folders)))
nimages = 0
for images_folder in images_folders:
    images = os.listdir(images_path + images_folder + '/')
    nimages += len(images)

print("Cantidad de imagenes a procesar: " + str(nimages))