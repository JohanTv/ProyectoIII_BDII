# ProyectoIII_BDII
## Integrantes

| Nombre y Apellidos | Código de alumno |
|-|-|
|Johan Tanta Villanueva |  |
|Jorge Nicho Galagarza	| 201810205 |
|Andres Riveros Soto    | 201810017 |


## RTree

Con las ayuda de la libreria Rtree creamos los indices Rtree para cada muestra de fotos. El indexfile es creado desde creation_rtree.ipynb, va a generar el archivo rtree_index. Este archivo servira para cargar el Rtree a memoria al momento de realizar las búsquedas. 

## Sequential
Creamos dataset_{size}.csv para cierta cantidad de imágenes y se encuentra en la carpeta data. A través de estos archivos que contienen el vector característico y la dirección de la foto resultante generamos los rtree_index_{size}. 

## Pruebas Funcionales KNN Search

Se implemento dos tipos de funciones para la busqueda KNN, el primero es el KNN-sequential y el segundo es el Knn-Rtree. Ambas funciones se encuentran dentro del archivo search.py. 

Por un lado, para  la busqueda Knn-Rtree se va a cargar a disco el archivo Rtree_index.idx  con la ayuda de la libreria Rtree . Se va a llamar al metodo `nearest` para encontrar los k mas cercanos, y luego en el archivo result_db.json se va a obtener la direccion de los fotos resultantes.

Por otro lado , la busqueda Knn Sequential, va a carga el archivo dataset_{size}.csv. Los objetos se van a introducir dentro un `min-heap` de tamaño k para obtener los k mas cercanos. 


Para las pruebas funcionales del KNN Search, la variable k tomó el valor de 8 . Se hizo el testing para cada tamano de imagenes, luego se grafico los tiempos del KNN tree y KNN Sequential



| Test  | Size  |KNN - Rtree | KNN- Secuencial| 
| :------------ |:---------------:| -----:| ------:|
| 1 | 100 |  0.1969 seconds|  0.1813 seconds |
| 2 | 200 |  0.0787 seconds | 0.2201 seconds|
| 3 | 400 |  0.0793 seconds| 0.1625 seconds  |
| 4 | 800 |  0.1285 seconds |  0.2302 seconds |
| 5 | 1600 | 0.0825 seconds  |  0.395 seconds|
| 6 | 3200 | 0.0918 seconds| 0.6639 seconds |
| 7 | 6400 | 0.1104 seconds | 1.2723 seconds |
| 8 | 12800 | 0.1453 seconds | 2.3845 seconds|

![imagen1](test/grafica_knn_search.png)
