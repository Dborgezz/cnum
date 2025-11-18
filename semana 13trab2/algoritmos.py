import math

def interpolacao_lagrange(x, y, x_alvo):
    soma = 0
    n = len(x)
    
    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo = termo * (x_alvo - x[j]) / (x[i] - x[j])
        soma += termo
    return soma

def regressao_linear(x, y):
    n = len(x)
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = sum(xi * yi for xi, yi in zip(x, y))
    soma_x_quad = sum(xi ** 2 for xi in x)
    
    denominador = n * soma_x_quad - soma_x ** 2
    
    if denominador == 0:
        return None, None

    a1 = (n * soma_xy - soma_x * soma_y) / denominador
    a0 = (soma_y - a1 * soma_x) / n
    
    return a1, a0

def funcao_chuva(r):
    if r >= 4: return 0 
    return r * (3 * (1 - r/4)**(1/7))

def regra_ponto_medio(func, a, b, n=100):
    h = (b - a) / n
    soma = 0
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        soma += func(x_mid)
    return soma * h

def regra_trapezio(func, a, b, n=100):
    h = (b - a) / n
    soma = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        x = a + i * h
        soma += func(x)
    return soma * h

def regra_simpson(func, a, b, n=100):
    if n % 2 != 0: n += 1
    h = (b - a) / n
    soma = func(a) + func(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            soma += 2 * func(x)
        else:
            soma += 4 * func(x)
            
    return soma * h / 3