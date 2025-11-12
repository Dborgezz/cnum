def medio(f, a, b):
    h = b - a
    return h * f((a + b) / 2)


def trapezio(f, a, b):
    h = b - a
    return h * (0.5 * f(a) + 0.5 * f(b))


def simpson(f, a, b):
    h = (b - a) / 2
    return h * ((1 / 3) * f(a) + (4 / 3) * f((a + b) / 2) + (1 / 3) * f(b))


def integral(metodo, f, a, b, n=1e-3):
    s = 0.0
    c = a
    d = a + n
    while d <= b:
        s += metodo(f, c, d)
        c = d
        d += n
    return s