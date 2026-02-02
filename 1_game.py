import random
# 功能: 1. (參數) 2. 名字 = 回傳答案
# 型態(分類): 1. 數字(int/float) 2.字串("")(str)
# 型態轉換: int() float() str()
# 的: .
my = int(input("可以輸入 0:剪刀 1:石頭 2:布"))
com = random.randint(0, 2)

# 轉換
# list(清單): l = [xxx, ooo, ddd]
#           編號    0    1    2
# 操作(查詢): l[編號]
trans = ["剪刀", "石頭", "布"]
print("我:" + trans[my])
print("電腦:" + trans[com])