import numpy as np
import matplotlib.pyplot as plt
import os

from algoritmos import regressao


def plot(x, y, v, num_img=1, title="Ajuste por Mínimos Quadrados", label="Ajuste f(x)"):
    output_dir = "semana 10/" 
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    x_vals = np.linspace(min(x) - 0.25, max(x) + 0.25, 400)
    
    A_coeffs = regressao(x, y, v)
    
    A_plot = v(x_vals)
    
    y_vals = A_plot @ A_coeffs 

    plt.figure(figsize=(7, 4))
    plt.scatter(x, y, color="blue", label="Pontos dados")
    plt.plot(x_vals, y_vals, color="red", label=label)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.tight_layout()
    
    filename = f"{output_dir}regressao_{num_img}.png"
    plt.savefig(filename, dpi=120, bbox_inches="tight")
    print(f"Gráfico salvo em: {filename}")
    plt.close()


def main():
    print("-- Atividade 1 --")
    x1 = np.array([-0.35, 0.15, 0.23, 0.35], dtype=float)
    y1 = np.array([0.20, -0.50, 0.54, 0.70], dtype=float)
    v1 = lambda x: np.column_stack((np.ones(len(x)), x))

    A1 = regressao(x1, y1, v1)
    
    print(f"Coeficientes [a1, a2]: {A1}")
    print(f"Equação: f(x) = {A1[0]:.4f} + ({A1[1]:.4f})x")
    plot(x1, y1, v1, 1, 
         title="Atividade 1: Ajuste Linear", 
         label="Ajuste Linear f(x)")

    print("\n-- Atividade 2 --")
    x2 = np.array([-1.94, -1.44, 0.03, 1.39], dtype=float)
    y2 = np.array([1.02, 0.59, -0.28, -1.04], dtype=float)
    v2 = lambda x: np.column_stack((np.ones(len(x)), x))
    
    A2 = regressao(x2, y2, v2)
    
    print(f"Coeficientes [a1, a2]: {A2}")
    print(f"Equação: f(x) = {A2[0]:.8f} + ({A2[1]:.8f})x")
    
    f_de_1 = A2[0] + A2[1] * 1.0
    print(f"f(1) = {f_de_1:.8f}")
    plot(x2, y2, v2, 2, 
         title="Atividade 2: Ajuste Linear", 
         label="Ajuste Linear f(x)")
    
    print("\n-- Atividade 3 --")
    x3 = np.array([0.01, 1.02, 2.04, 2.95, 3.55], dtype=float)
    y3 = np.array([1.99, 4.55, 7.20, 9.51, 10.82], dtype=float)
    v3 = lambda x: np.column_stack((np.ones_like(x), x, x**2))
    
    A3 = regressao(x3, y3, v3)
    
    print(f"Coeficientes [c, b, a]: {A3}")
    print(f"Equação: y = {A3[2]:.8f}x^2 + {A3[1]:.8f}x + {A3[0]:.8f}")
    plot(x3, y3, v3, 3, 
         title="Atividade 3: Ajuste Parabólico", 
         label="Ajuste Parabólico f(x)")

    print("\n-- Atividade 4 --")
    x4 = np.array([0.0, 0.1, 0.2, 0.3, 0.4], dtype=float)
    y4 = np.array([31, 35, 37, 33, 28], dtype=float)

    print(" (a) Ajuste Trigonométrico")
    v4a = lambda x: np.column_stack((np.ones_like(x), np.sin(2*np.pi*x), np.cos(2*np.pi*x)))
    
    A4a = regressao(x4, y4, v4a)
    
    print(f"Coeficientes [a, b, c]: {A4a}")
    print(f"  a = {A4a[0]:.6f}, b = {A4a[1]:.6f}, c = {A4a[2]:.6f}")
    plot(x4, y4, v4a, 4, 
         title="Atividade 4a: Ajuste Trigonométrico",
         label="Ajuste Trigonométrico f(x)")

    print("\n (b) Ajuste Cúbico")
    v4b = lambda x: np.column_stack((np.ones_like(x), x, x**2, x**3))
    
    A4b = regressao(x4, y4, v4b)
    
    print(f"Coeficientes [a, b, c, d]: {A4b}")
    print(f"  a = {A4b[0]:.6f}, b = {A4b[1]:.6f}, c = {A4b[2]:.6f}, d = {A4b[3]:.6f}")
    plot(x4, y4, v4b, 5, 
         title="Atividade 4b: Ajuste Cúbico",
         label="Ajuste Cúbico f(x)")


if __name__ == "__main__":
    main()
    