from rtree import index

p = index.Property()
p.dimension = 2 #D
p.buffering_capacity = 3 #M, m = M/2
p.dat_extension = 'data'
p.idx_extension = 'index'

idx = index.Index('2d_index',properties=p)

#retornar elementos de la interseccion con el rectangulo 
Q=(4, 4, 6, 8)
lres = [n for n in  idx.intersection(Q)]
print("Resultado Inter: ", lres)

#retornar los k vecinos de Q
Q=(1, 2, 1, 2)
k = 3
lres = list(idx.nearest(coordinates=Q, num_results=k))
print("Resultado Knn: ", lres)