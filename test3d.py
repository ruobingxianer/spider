import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 准备数据
# 给定的数据
data = [
    [1.151, 1.018, 1.0845, 1],
    [1.061, 1.062, 1.0615, 1],
    [0.89, 0.708, 0.799, 1],
    [1.265, 1.538, 1.4015, 1],
    [4.029, 3.291, 3.66, 2],
    [3.74, 2.742, 3.241, 2],
    [4.01, 2.761, 3.3855, 2],
    [3.812, 3.309, 3.5605, 2],
    [3.168, 2.215, 2.6915, 3],
    [3.417, 1.866, 2.6415, 3],
    [3.428, 2.076, 2.752, 3],
    [2.955, 2.311, 2.633, 3],
    [0.991, 4.151, 2.571, 4],
    [0.945, 4.291, 2.618, 4],
    [0.729, 4.16, 2.4445, 4],
    [0.772, 4.54, 2.656, 4]
]

# 分离数据到 x, y, z, i 数组
x = [row[0] for row in data]
y = [row[1] for row in data]
z = [row[2] for row in data]
i = [row[3] for row in data]


# 创建一个新的图和一个子图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图，使用z值来决定颜色
scatter = ax.scatter(x, y, z, c=i, cmap='viridis')  # 'viridis'是matplotlib中的一种颜色映射

# 添加颜色条
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Z Value')

# 设置图表标题和坐标轴标签
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")

# 显示图表
plt.show()