# 当一条支路最小安全距离是最大时，其是最大，也就是说只需要存储最小路径
# 对角转移
# 首先需要找到危险单元
data = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
ones = []
for idx, row in enumerate(data):
    if not any(row):
        continue
    for v in row:
        if v:
            ones.append((idx, v))
