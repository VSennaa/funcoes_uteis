import matplotlib.pyplot as ptl
from sklearn.cluster import KMeans
import numpy as np

def cotovelo(dataset, graph=True):
    """
    Aplica o método do cotovelo para determinar o número ideal de clusters,
    com detecção automática do ponto de inflexão (cotovelo).

    Parâmetros:
    -----------
    dataset : array-like ou DataFrame
        Conjunto de dados a ser analisado.
    graph : bool, opcional (default=True)
        Se True, exibe o gráfico do método do cotovelo.

    Retorno:
    --------
    k_ideal : int
        Valor de k considerado ideal pelo método do cotovelo.
    """
    inercias = []
    K_range = range(1, 10)
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=7)
        kmeans.fit(dataset)
        inercias.append(kmeans.inertia_)

    # Método geométrico para encontrar o cotovelo
    x = np.array(list(K_range))
    y = np.array(inercias)

    # reta entre primeiro e último ponto
    linha = np.array([x[-1] - x[0], y[-1] - y[0]])
    linha = linha / np.linalg.norm(linha)
    pontos = np.stack((x - x[0], y - y[0]), axis=1)
    distancias = np.abs(np.cross(pontos, linha))
    k_ideal = x[np.argmax(distancias)]

    if graph:
        ptl.figure(figsize=(8, 5))
        ptl.plot(K_range, inercias, 'bo-', label='Inércia')
        ptl.axvline(k_ideal, color='red', linestyle='--', label=f'k ideal = {k_ideal}')
        ptl.xlabel('Número de clusters (k)')
        ptl.ylabel('Inércia')
        ptl.title('Método do Cotovelo')
        ptl.xticks(K_range)
        ptl.grid(True)
        ptl.legend()
        ptl.show()

    return k_ideal
