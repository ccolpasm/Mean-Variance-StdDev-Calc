

import numpy as np

def calculate(list):
    # Verificar si la lista tiene exactamente 9 elementos
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la lista en un arreglo Numpy 3x3
    matrix = np.array(list).reshape(3, 3)
    
    # Calcular las estadísticas por fila (axis=1), por columna (axis=0) y para toda la matriz (flattened)
    calculations = {
        'mean': [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix).tolist()
        ],
        'variance': [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix).tolist()
        ],
        'standard deviation': [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).tolist()
        ],
        'max': [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).tolist()
        ],
        'min': [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).tolist()
        ],
        'sum': [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).tolist()
        ]
    }
    
    return calculations