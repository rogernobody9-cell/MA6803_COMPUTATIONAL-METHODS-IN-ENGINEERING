# 数值解，可能是近似解
import numpy as np

coefficients = [6, -19, -28, 83 ,12]
roots = np.roots(coefficients)
print('方程的根为：')
for root in roots:
    print(f'{root:.4f}')

# 符号解，或者说解析解
# from sympy import symbols,solve
#
# x = symbols('x')
# equation = 6*x**4 - 19*x**3 - 28*x**2 + 83*x + 12
# result = solve(equation,x)
# print(f'精确解为：{result}')

