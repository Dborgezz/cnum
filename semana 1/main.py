#a.x²+b.x+c
"""
Raíz da Equação de Segundo Grau
"""
import math

def raízes(a, b, c):
    delta = b**2 - 4*a*c
    if a==0:
        x=-c/b
        return [x, x]

    elif delta < 0:
        return None
    elif delta == 0:
        x=-b / (2*a)
        return [x, x]
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
    return [x1, x2]

def main():
    X = raízes(0, 2, 1)
    print(X)

if __name__ == "__main__":
    main()