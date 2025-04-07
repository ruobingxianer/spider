import networkx as nx
import matplotlib.pyplot as plt

# 创建无向图
G = nx.Graph()

# 添加所有节点（显式定义确保孤立节点可见）
nodes = [1, 2, 3, 4, 5, 6, 7]
G.add_nodes_from(nodes)

# 添加边
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (6, 7)]
G.add_edges_from(edges)

# 设置布局与绘图参数
pos = nx.spring_layout(G, seed=42)  # 使用弹簧布局确保连通分量分离
nx.draw(G, pos)

plt.title("无向图示例（包含两个连通分量）")
plt.show()