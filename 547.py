isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


class DSU:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        la = self.find(a)
        lb = self.find(b)

        if la == lb:
            return
        if self.size[la] < self.size[lb]:
            la, lb = lb, la

        self.parent[lb] = la
        self.size[la] += self.size[lb]


dsu = DSU(len(isConnected))
arr = []
for idx, row in enumerate(isConnected):
    for l_idx, i in enumerate(row):
        if l_idx == idx:
            continue
        if i == 1:
            arr.append((idx, l_idx))
unique_edges = list({tuple(sorted(e)) for e in arr})

for row in unique_edges:
    dsu.union(*row)

for i in range(len(isConnected)):
    dsu.find(i)
print(len(set(dsu.parent)))
