# 摆线是由圆轮上的一个点沿着x轴滚动时所描绘的曲线，圆轮的半径为r。该曲线可以用参数形式表示为下列方程：
# x = r(θ – sin θ)
# y = r(1 – cos θ)
# 使用这些方程绘制半径为r = 10且0 ≤ θ ≤ 4π的摆线。

import numpy as np
import matplotlib.pyplot as plt

r = 10
theta_start = 0
theta_end = 4 * np.pi
theta = np.linspace(theta_start, theta_end, 1000)
x = r * (theta - np.sin(theta))
y = r * (1 - np.cos(theta))
fig,ax = plt.subplots()
ax.plot(x, y, label = 'Cycloid', color = 'blue', linewidth = 2)
ax.axhline(y = 0, color = 'red', linewidth = 1)
ax.set_aspect('equal')
ax.set_title(f'Cycloid(r={r},θ≤ θ ≤4π)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, alpha = 0.3, linestyle = '--')
ax.legend()
plt.show()