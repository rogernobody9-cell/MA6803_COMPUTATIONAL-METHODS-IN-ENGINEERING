# 使用矩阵思维
import numpy as np

A = np.array([[7, 14 ,-6],
              [12, -5 ,9],
              [-5, 7 ,15]])
B = np.array([95, -50, 145])
try:
    X = np.linalg.solve(A,B)
    print(f'解为：x={X[0]:.1f}，y={X[1]:.1f}，z={X[2]:.1f}')
except np.linalg.LinAlgError:
    print('这个方程组无解或有无数解（矩阵不可逆）')
print(f"验证计算 (A @ X): {A @ X}")
print(f"原始 B: {B}")