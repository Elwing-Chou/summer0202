x = [30, 20, 30]
print(x)

# 取編號
# [列, 列, 列]
x = [[2, 5], [1, 4]]
print(x)
print(x[0])
print(x[0][1])

# 迴圈
test = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]
print(test[1][2])
print(test[2][1])

for i in range(4):
    for j in range(3):
        test[i][j] = 0

# 初始化
print([1, 2] * 3)
print(["hello" for i in range(5)])
print([[0] * 3 for i in range(5)])