import numpy as np
from algoritmos import dp, dr, dc

def regressao(x, y, v):
    A = v(x)
    coeffs = np.linalg.lstsq(A, y, rcond=None)[0]
    return coeffs
# -------------------------------------------------


def main():
    print("-- Atividade 1 --")
    h1 = 1e-2
    h2 = 1e-3
    eps = np.finfo(float).eps

    # --- Primeira função (f(x) = sin(x) - 2, em x=2) ---
    print("\nPara f'(x) onde f(x) = sin(x) - 2, em x=2:")
    f = lambda x: np.sin(x) - 2
    fd = lambda x: np.cos(x)
    x0_f = 2
    
    print("Diferença progressiva:")
    print(f"h = 0.01  | f'(x)=", dp(f, x0_f, h1))
    print(f"h = 0.001 | f'(x)=", dp(f, x0_f, h2))
    
    print("Diferença regressiva:")
    print(f"h = 0.01  | f'(x)=", dr(f, x0_f, h1))
    print(f"h = 0.001 | f'(x)=", dr(f, x0_f, h2))

    print("Diferença central:")
    print(f"h = 0.01  | f'(x)=", dc(f, x0_f, h1))
    print(f"h = 0.001 | f'(x)=", dc(f, x0_f, h2))
    
    # Bloco "Derivada com SciPy:" removido
    
    print("Derivada analítica (Exata):")
    exata_f = fd(x0_f)
    print(f"f'(x) = cos(2) = {exata_f:.5f}")


    print("\nPara f'(x) onde f(x) = e^(-x) - 1, em x=1:")
    g = lambda x: np.exp(-x) - 1
    gd = lambda x: -np.exp(-x)
    x0_g = 1

    print("Diferença progressiva:")
    print(f"h = 0.01  | f'(x)=", dp(g, x0_g, h1))
    print(f"h = 0.001 | f'(x)=", dp(g, x0_g, h2))

    print("Diferença regressiva:")
    print(f"h = 0.01  | f'(x)=", dr(g, x0_g, h1))
    print(f"h = 0.001 | f'(x)=", dr(g, x0_g, h2))

    print("Diferença central:")
    print(f"h = 0.01  | f'(x)=", dc(g, x0_g, h1))
    print(f"h = 0.001 | f'(x)=", dc(g, x0_g, h2))

    # Bloco "Derivada com SciPy:" removido
    
    print("Derivada analítica (Exata):")
    exata_g = gd(x0_g)
    print(f"f'(x) = -e^(-1) = {exata_g:.5f}")

    
    # --- Atividade 2 ---
    print("\n\n-- Atividade 2 --")
    
    vi = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    vo = np.array([0.0, 1.05, 1.83, 2.69, 3.83, 4.56, 5.49, 6.56, 6.11, 7.06, 8.29])
    h_vi = 0.5 

    print("--- Resultados para vi = 1 ---")
    
    vo_i_1 = vo[2]    
    vo_ant_1 = vo[1]  
    vo_prox_1 = vo[3] 
    
    G_a_1 = (vo_prox_1 - vo_i_1) / h_vi
    G_b_1 = (vo_i_1 - vo_ant_1) / h_vi
    G_c_1 = (vo_prox_1 - vo_ant_1) / (2 * h_vi)
    
    v_func = lambda x: np.column_stack((x, x**3))
    coeffs = regressao(vi, vo, v_func) 
    a1, a3 = coeffs[0], coeffs[1]
    
    G_d_func = lambda v: a1 + 3 * a3 * (v**2)
    G_d_1 = G_d_func(1.0)

    print(f"  a) Progressiva: {G_a_1:.2f} ")
    print(f"  b) Regressiva:  {G_b_1:.2f} ")
    print(f"  c) Central:     {G_c_1:.2f} ")
    print(f"  d) Analítica:   {G_d_1:.2f} ")

    
    print("\n--- Resultados para vi = 4.5 ---")
    
    vo_i_45 = vo[9]   
    vo_ant_45 = vo[8]  
    vo_prox_45 = vo[10] 
    
    G_a_45 = (vo_prox_45 - vo_i_45) / h_vi
    G_b_45 = (vo_i_45 - vo_ant_45) / h_vi
    G_c_45 = (vo_prox_45 - vo_ant_45) / (2 * h_vi)
    
    G_d_45 = G_d_func(4.5)
    
    print(f"  a) Progressiva: {G_a_45:.2f} ")
    print(f"  b) Regressiva:  {G_b_45:.2f} ")
    print(f"  c) Central:     {G_c_45:.2f} ")
    print(f"  d) Analítica:   {G_d_45:.2f} ")


if __name__ == "__main__":
    main()
    