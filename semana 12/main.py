import numpy as np
from scipy.integrate import quad


from algoritmos import (
    medio,
    trapezio,
    simpson,
    integral,
)

def main():
   
    print("-- Atividade 1 --")
    

    funcs = [
        ('a', lambda x: np.exp(-x), 0, 1),
        ('b', lambda x: x**2, 0, 1),
        ('c', lambda x: x**3, 0, 1),
        ('d', lambda x: x * np.exp(-x**2), 0, 1),
        ('e', lambda x: 1 / (x**2 + 1), 0, 1),
        ('f', lambda x: x / (x**2 + 1), 0, 1),
    ]


    print(f"\nResultados (usando 'integral' com h=1e-3):")
    print(f"{'f':^3} | {'Ponto médio':^15} | {'Trapézio':^15} | {'Simpson':^15} | {'SciPy':^15}")
    print("-" * 69)

  
    for (label, f, a, b) in funcs:
        r_med = integral(medio, f, a, b)
        r_trap = integral(trapezio, f, a, b)
        r_simp = integral(simpson, f, a, b)
        r_scipy, _ = quad(f, a, b)
        
        print(f"{label:^3} | {r_med:^15.8f} | {r_trap:^15.8f} | {r_simp:^15.8f} | {r_scipy:^15.8f}")


    print("\n\n-- Atividade 2 --")
    
    # Função: f(x) = e^(4 - x^2)
    f_2 = lambda x: np.exp(4 - x**2)
    a_2 = 2.0
    b_2 = 5.0
    

    n_list = [3, 5, 7, 9]
    
   
    print(f"\nResultados para a integral de e^(4-x^2) de {a_2} a {b_2}")
    print(f"{'n':>3} | {'Ponto médio':^15} | {'Trapézios':^15} | {'Simpson':^15}")
    print("-" * 53)
    
    for n_val in n_list:
       
        h = (b_2 - a_2) / n_val
        
      
        res_medio = integral(medio, f_2, a_2, b_2, n=h)
        res_trap = integral(trapezio, f_2, a_2, b_2, n=h)
        res_simp = integral(simpson, f_2, a_2, b_2, n=h)
        
 
        print(f"{n_val:>3} | {res_medio:^15.7f} | {res_trap:^15.7f} | {res_simp:^15.7f}")


    r_scipy, err_scipy = quad(f_2, a_2, b_2)
    print(f"\nValor (SciPy): {r_scipy:.7f}")


if __name__ == "__main__":
    main()