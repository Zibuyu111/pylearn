"""
题目描述
给定 n 个点（编号 0 ~ n-1），给出 m 条无向边，每条边连接两个点。
求：整张图一共有多少个互不连通的连通块。
输入样例
plaintext
n=5, m=3
边：
0 1
1 2
3 4
输出样例
2
解释：{0,1,2}、{3,4} 两个连通块。
"""

"""
#前期思考题目描述
给定 n 个点（编号 0 ~ n-1），给出 m 条无向边，每条边连接两个点。
求：整张图一共有多少个互不连通的连通块。
输入样例
plaintext
n=5, m=3
边：
0 1
1 2
3 4
输出样例
2
解释：{0,1,2}、{3,4} 两个连通块。
print("____________")
n,m = input().split()
ls = []
for _ in range(m):
    a,b = input().split()
    ls.append((a,b))

#初始化，每个节点的父节点都是自己
parent = [i for i in range(m)]
#实现find函数
def find(x):
    if parent[x] != x:#父节点不是自己
        parent[x] = find(parent[x])#找到输入节点的根节点
    return parent[x]

#实现union,按大小合并
def union(u,v):
    ru = find(u)
    rv = find(v)

    if ru == rv:#判断这两个分支的端点是否一致
        return
    if size[ru] < size[rv]:#要获得这个size
        ru, rv = rv, ru

    parent[rv] = ru
    size[ru] += size[rv]
"""


class DSU:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 折叠树
        return self.parent[x]

    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)
        if ru == rv:
            return
        if self.size[ru] < self.size[rv]:
            ru, rv = rv, ru
        self.parent[rv] = ru
        self.size[ru] += self.size[rv]


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
dsu = DSU(n)
for u, v in edges:
    dsu.union(u, v)

cnt = 0
for i in range(n):
    dsu.find(i)
print(len(set(dsu.parent)))
