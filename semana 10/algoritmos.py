import numpy as np

def regressao(x, y, v):
    V = v(x)
    Vt = V.T
    A = np.linalg.inv(Vt @ V) @ (Vt @ y)
    return A