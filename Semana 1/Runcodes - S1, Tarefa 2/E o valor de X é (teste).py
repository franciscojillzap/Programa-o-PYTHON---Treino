import sympy as sp
x=sp.Symbol("x")
equação=sp.Eq(9*x - 4*x + 10, 0)
valor_x=sp.solve(equação, x)
print(valor_x)


