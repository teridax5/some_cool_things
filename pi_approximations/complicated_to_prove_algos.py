def pi_evaluation():
    """Algorithm Brent-Salamin proved by using elliptical
    integrals and AGM."""
    a = 1
    b = 1/(2**0.5)
    t = 0.25
    p = 1

    while abs(a-b) > 10**(-10):
        a_new, b_new = (a+b)/2, (a*b)**0.5
        t = t - p*(a-a_new)**2
        a, b = a_new, b_new
        p = 2*p
    return (a+b)**2/(4*t)
