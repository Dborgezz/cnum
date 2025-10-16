from algoritmos import *
import numpy as np


def atividade1():
    E = 500.125
    K = 272.975

    f = lambda T: 5.67e-8 * T**4 + 0.4 * (T - K) - E

    T = bissecao(f, 200, 400)
    print(f"Atividade 1 -> Temperatura da placa: T = {T:.10f} K")


def atividade2():
    A = np.array([
        [17, -2, -3],
        [-5, 21, -2],
        [-5, -5, 22]
    ], dtype=float)

    b = np.array([500, 200, 300], dtype=float)

    R = gauss_seidel(A, b)
    print("Atividade 2 -> Tensões nominais:")
    print(f"R1 = {R[0]:.6f}, R2 = {R[1]:.6f}, R3 = {R[2]:.6f}")


def atividade3():
    A = np.array([
        [20, 10],
        [10, 20]
    ], dtype=float)
    b = np.array([100, 100], dtype=float)

    I = gauss_seidel(A, b)
    I1, I2 = I
    I_R3 = I1 + I2  # soma das correntes

    print("Atividade 3 -> Corrente no resistor R3:")
    print(f"I_R3 = {I_R3:.4f} A")



def atividade4():
    E1, E2 = 0.01753, 0.00254

    def F(X):
        T1, T2 = X
        return [
            T1**4 + 0.06823*T1 - (T2**4 + 0.05848*T2) - E1,
            T1**4 + 0.05848*T1 - (2*T2**4 + 0.11696*T2) - E2
        ]

    def J(X):
        T1, T2 = X
        return [
            [4*T1**3 + 0.06823, -4*T2**3 - 0.05848],
            [4*T1**3 + 0.05848, -8*T2**3 - 0.11696]
        ]

    X0 = np.array([0.2, 0.1])
    T = newton_raphson_system(F, J, X0)

    print("Atividade 4 -> Temperaturas de equilíbrio:")
    print(f"T1 = {T[0]:.6f}, T2 = {T[1]:.6f}")


if __name__ == "__main__":
    print("\n=== Semana 8 - Métodos Numéricos ===\n")
    atividade1()
    print("\n-----------------------------------\n")
    atividade2()
    print("\n-----------------------------------\n")
    atividade3()
    print("\n-----------------------------------\n")
    atividade4()