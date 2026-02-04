i = 0
while i < 10:
    print("hello")
    i = i + 1

# 清單 []
# 編號: 0 1 2
# 查詢: 清單名字[編號]
# i 0 1 2
total = 0
scores = [20, 30, 40]
i = 0
while i < len(scores):
    total = total + scores[i]
    i = i + 1
print(total)

total = 0
scores = [20, 30, 40]
for s in scores:
    total = total + s
print(total)

# 1 + 2 + 3...+ 10
# range(5): [0, 1, 2, 3, 4]
total = 0
for i in range(10):
    total = total + (i + 1)
print(total)