# funcoes_uteis/n_cluster.py
import matplotlib.pyplot as ptl
from sklearn.cluster import KMeans

def cotovelo(dataset):
    inercias = []
    K_range = range(1, 10)
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=7)
        kmeans.fit(dataset)
        inercias.append(kmeans.inertia_)  

    ptl.figure(figsize=(8, 5))
    ptl.plot(K_range, inercias, 'bo-')
    ptl.xlabel('Número de clusters (k)')
    ptl.ylabel('Inércia')
    ptl.title('Método do Cotovelo')
    ptl.xticks(K_range)
    ptl.grid(True)
    ptl.show()
