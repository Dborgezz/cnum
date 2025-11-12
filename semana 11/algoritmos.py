def dp(f, x, h):
    return (f(x + h) - f(x)) / h


def dr(f, x, h):
    return (f(x) - f(x - h)) / h


def dc(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)