import numpy as np


def bissecao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")
    for i in range(max_iter):
        m = (a + b) / 2
        if abs(f(m)) < tol or (b - a) / 2 < tol:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m



def ponto_fixo(g, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x1



def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy()

    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / A[i][i]
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x
    return x


def newton_raphson_system(F, J, x0, tol=1e-6, max_iter=100):
    x = x0.copy()
    for i in range(max_iter):
        Fx = np.array(F(x))
        Jx = np.array(J(x))
        dx = np.linalg.solve(Jx, -Fx)
        x = x + dx
        if np.linalg.norm(dx, ord=np.inf) < tol:
            return x
    return x