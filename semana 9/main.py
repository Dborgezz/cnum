import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, lagrange
import os

def plot(x, y, num_img=1, title_suffix="", x_label="x", y_label="y"):
    x_vals = np.linspace(min(x) - 0.25, max(x) + 0.25, 400)
    
    p = lagrange(x, y)
    yn = np.polyval(p, x_vals) 
    yl = np.polyval(p, x_vals) 
    yp = np.polyval(p, x_vals) 
    
    spline = CubicSpline(x, y, bc_type="natural")
    ys = spline(x_vals)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, yn, label="Newton", linewidth=2)
    plt.plot(x_vals, yl, label="Lagrange", linestyle="--", linewidth=2)
    plt.plot(x_vals, yp, label="Polinomial", linestyle=":", linewidth=2)
    plt.plot(x_vals, ys, label="Spline cúbica", linewidth=2.5, linestyle="-.")
    
    plt.scatter(x, y, label="Pontos", zorder=5, color='red', s=50)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f"Interpolação: {title_suffix}")
    plt.legend()
    plt.grid(True, which="both", linestyle=":")
    plt.tight_layout()
    
    output_dir = "semana 9/" 
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filename = f"{output_dir}interpolacao_{num_img}.png"
    plt.savefig(filename, dpi=120, bbox_inches="tight")
    print(f"Gráfico salvo em: {filename}")
    plt.close()


def main():
    print("-- Atividade 1 --")
    x1 = np.array([-2.0, 0.0, 1.0, 2.0], dtype=float)
    y1 = np.array([-47.0, -3.0, 4.0, 41.0], dtype=float)
    xr1 = np.array([-1.0, 0.5, 1.5], dtype=float)

    p1 = lagrange(x1, y1)
    yn1 = np.polyval(p1, xr1)
    yl1 = np.polyval(p1, xr1)
    yp1 = np.polyval(p1, xr1)

    spline1 = CubicSpline(x1, y1, bc_type="natural")
    ys1 = spline1(xr1)

    print("Resultados (N=Newton, L=Lagrange, P=Polinomial, S=Spline):")
    for xi, n, l, p, s in zip(xr1, yn1, yl1, yp1, ys1):
        print(f"x = {xi:>4}:  N={n: .6f} | L={l: .6f} | P={p: .6f} | S={s: .6f}")
    plot(x1, y1, 1, title_suffix="Atividade 1 (f(x) = -3 + 2x + 5x³)")
    
    
    print("\n-- Atividade 2  --")
    x2 = np.array([-1.0, 0.5, 1.0, 1.25], dtype=float)
    y2 = np.array([1.25, 0.5, 1.25, 1.8125], dtype=float)
    xr2 = np.array([-0.5, 0.0, 0.25], dtype=float)

    p2 = lagrange(x2, y2)
    yn2 = np.polyval(p2, xr2)
    yl2 = np.polyval(p2, xr2)
    yp2 = np.polyval(p2, xr2)

    spline2 = CubicSpline(x2, y2, bc_type="natural")
    ys2 = spline2(xr2)

    print("Resultados (N=Newton, L=Lagrange, P=Polinomial, S=Spline):")
    for xi, n, l, p, s in zip(xr2, yn2, yl2, yp2, ys2):
        print(f"x = {xi:>4}:  N={n: .6f} | L={l: .6f} | P={p: .6f} | S={s: .6f}")
    plot(x2, y2, 2, title_suffix="Atividade 2 (f(x) = 0.25 + x²)")
    
    
    print("\n-- Atividade 3a  --")
    x3a = np.array([-50.0, -5.0, 5.0, 75.0], dtype=float)
    y3a = np.array([-300.0, -50.0, 180.0, 350.0], dtype=float)
    xr3a = np.array([0.0], dtype=float) 

    p3a = lagrange(x3a, y3a)
    yn3a = np.polyval(p3a, xr3a)
    yl3a = np.polyval(p3a, xr3a)
    yp3a = np.polyval(p3a, xr3a)

    spline3a = CubicSpline(x3a, y3a, bc_type="natural")
    ys3a = spline3a(xr3a)

    print("Resultados (N=Newton, L=Lagrange, P=Polinomial, S=Spline):")
    for xi, n, l, p, s in zip(xr3a, yn3a, yl3a, yp3a, ys3a):
        print(f"H = {xi:>4}:  N={n: .6f} | L={l: .6f} | P={p: .6f} | S={s: .6f}")
    plot(x3a, y3a, 3, title_suffix="Atividade 3a (H vs B)", x_label="H (A/m)", y_label="B (mT)")


    print("\n-- Atividade 3b  --")
    x3b = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
    y3b = np.array([80, -60, 40, -30, 20, -10, 5, -2.5, 1.25, -0.625, 0.3125], dtype=float)
    xr3b = np.array([8.5], dtype=float) 

    p3b = lagrange(x3b, y3b)
    yn3b = np.polyval(p3b, xr3b)
    yl3b = np.polyval(p3b, xr3b)
    yp3b = np.polyval(p3b, xr3b)

    spline3b = CubicSpline(x3b, y3b, bc_type="natural")
    ys3b = spline3b(xr3b)

    print("Resultados (N=Newton, L=Lagrange, P=Polinomial, S=Spline):")
    for xi, n, l, p, s in zip(xr3b, yn3b, yl3b, yp3b, ys3b):
        print(f"T = {xi:>4}:  N={n: .6f} | L={l: .6f} | P={p: .6f} | S={s: .6f}")
    plot(x3b, y3b, 4, title_suffix="Atividade 3b (T vs H)", x_label="T (s)", y_label="H (A/m)")
  


if __name__ == "__main__":
    main()