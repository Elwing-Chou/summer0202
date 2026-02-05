s = [30, 50, 20, 10]

maxv, maxi = float("-inf"), -1
for i in range(4):
    if s[i] > maxv:
        maxv, maxi = s[i], i

print(maxv, maxi)