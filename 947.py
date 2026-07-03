stones = [[0, 0]]
# 一个单位存在行与列两个属性，可以看作是两分支，转换成树的问题就可以利用并查集求解


class DSU:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        lu = self.find(a)
        lv = self.find(b)

        if lu == lv:
            return
        if lu < lv:
            lu, lv = lv, lu

        self.size[lu] += self.size[lv]
        self.parent[lv] = lu


# 思考问题删除那个节点？
# 父节点表示连接二者，在只有三个单位的情况下，删除父节点，子节点便符合孤立要求
# union是顺序读入，一节点虽为子节点会存在两个节点的情况，怎么解决？
# 首先考虑一个问题，节点是如何被合并的。

dsu = DSU(len(stones))
for idx_i, i in enumerate(stones):
    # 判断是否为同一行
    # 直接暴力？
    # 先尝试暴力
    if idx_i == len(stones) - 1:
        break
    for idx_j, j in enumerate(stones[idx_i + 1 :]):
        print(stones[idx_i + 1 :])
        if i[0] == j[0] or i[1] == j[1]:
            # print(idx_i, idx_j + idx_i + 1)
            dsu.union(idx_i, idx_j + idx_i + 1)
# print(dsu.parent)
# 也就是说，题目存在绝对孤立，删除父节点后孤立
# 题目的示例有个小细节，移除是从后往前，所以是删除子节点，而不是我认为的父节点
# 合并之后父节点不为自己的删掉即可？
cnt = 0
for i in range(len(stones)):
    if i != dsu.parent[i]:
        cnt += 1
print(cnt)
