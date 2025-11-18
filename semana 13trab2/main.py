import algoritmos as alg
import math
import numpy as np

# Função movida para cá pois depende do numpy
def estimar_rl_circuito(t_vals, i_vals, t_alvo, R, L, grau_polinomio):
    coeffs = np.polyfit(t_vals, i_vals, grau_polinomio)
    p = np.poly1d(coeffs)
    i_estimado = p(t_alvo)
    
    derivada_poly = np.polyder(p)
    di_dt_estimado = derivada_poly(t_alvo)
    
    v_estimado = L * di_dt_estimado + R * i_estimado
    
    return v_estimado

def main():
    print("=== EXECUÇÃO DO SEGUNDO TRABALHO ===\n")

    print("--- Atividade 1 ---")
    temps = [4.9, 3.3, 3.0, 2.0]
    metros = [1.5, 2.0, 2.2, 3.0]
    novas_serpentinas = [1.75, 2.5, 2.75, 3.2]
    
    respostas_atv1 = []
    for x_alvo in novas_serpentinas:
        y_pred = alg.interpolacao_lagrange(metros, temps, x_alvo)
        respostas_atv1.append(y_pred)
    
    print(f"Temperaturas: {[round(v, 2) for v in respostas_atv1]}\n")

    print("--- Atividade 2 ---")
    t_atv2 = [0.2, 0.5, 0.7, 1.0]
    i_atv2 = [0.8187, 1.5815, 1.9354, 2.2905]
    
    i_03 = alg.interpolacao_lagrange(t_atv2, i_atv2, 0.3)
    i_09 = alg.interpolacao_lagrange(t_atv2, i_atv2, 0.9)
    
    print(f"I(0.3) = {i_03:.6f} A")
    print(f"I(0.9) = {i_09:.6f} A\n")

    print("--- Atividade 3 ---")
    y_outono = [38, 40, 42, 44, 46]
    x_outono = [1, 1.25, 1.5, 1.75, 2]
    a1_out, a0_out = alg.regressao_linear(x_outono, y_outono)
    print(f"Outono: a1={a1_out:.2f}, a0={a0_out:.2f}")

    y_inverno = [40, 44, 48, 52, 56]
    x_inverno = [1, 1.5, 2, 2.5, 3]
    a1_inv, a0_inv = alg.regressao_linear(x_inverno, y_inverno)
    print(f"Inverno: a1={a1_inv:.2f}, a0={a0_inv:.2f}")

    y_prim = [36, 39, 42, 45, 48]
    x_prim = [1, 1.15, 1.3, 1.45, 1.6]
    a1_prim, a0_prim = alg.regressao_linear(x_prim, y_prim)
    print(f"Primavera: a1={a1_prim:.2f}, a0={a0_prim:.2f}\n")

    print("--- Atividade 4 ---")
    v_vals = [5.1, 10.3, 15.2, 20.1, 24.7, 30.5]
    i_vals = [0.5, 1.1, 1.5, 2.2, 2.5, 3.1]
    
    req, b = alg.regressao_linear(i_vals, v_vals)
    print(f"Req = {req:.6f} Ohms")
    print(f"b   = {b:.6f} V\n")

    print("--- Atividades 5, 6, 7 ---")
    t_dados = [0.0, 0.1, 0.2, 0.3, 0.4]
    i_dados = [0.00, 0.82, 1.36, 1.60, 1.73]
    R = 5
    L = 0.1
    t_estimar = 0.5
    
    # Note que agora chamamos a função localmente, e não mais do 'alg'
    v_atv5 = estimar_rl_circuito(t_dados, i_dados, t_estimar, R, L, 1)
    print(f"V(0.5) Linear = {v_atv5:.5f} V")

    v_atv6 = estimar_rl_circuito(t_dados, i_dados, t_estimar, R, L, 2)
    print(f"V(0.5) Quadrático = {v_atv6:.5f} V")

    v_atv7 = estimar_rl_circuito(t_dados, i_dados, t_estimar, R, L, 3)
    print(f"V(0.5) Cúbico = {v_atv7:.5f} V\n")

    print("--- Atividades 8, 9, 10 ---")
    raios = [1.25, 2.55, 3.15, 3.95]
    
    print("Ponto Médio:")
    for r in raios:
        integral = alg.regra_ponto_medio(alg.funcao_chuva, 0, r, n=100)
        q = 2 * math.pi * integral
        print(f"r={r}: Q(r)={q:.6f}")

    print("\nTrapézio:")
    for r in raios:
        integral = alg.regra_trapezio(alg.funcao_chuva, 0, r, n=100)
        q = 2 * math.pi * integral
        print(f"r={r}: Q(r)={q:.6f}")

    print("\nSimpson:")
    for r in raios:
        integral = alg.regra_simpson(alg.funcao_chuva, 0, r, n=100)
        q = 2 * math.pi * integral
        print(f"r={r}: Q(r)={q:.6f}")

if __name__ == "__main__":
    main()