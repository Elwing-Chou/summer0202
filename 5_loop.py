import random

low, high = 1, 100
ans = random.randint(low, high)
# True False
while True:
    s = str(low) + "-" + str(high)
    guess = int(input(s))
    if guess > ans:
        print("too big")
        high = guess
    elif guess < ans:
        print("too small")
        low = guess
    else:
        print("ok")
        break