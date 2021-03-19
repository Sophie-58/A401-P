scores = []
n = input("請輸入學生數量：")
n = int(n)
high = 0
highn = ("xx")
low = 100
lown = ("xx")
total = 0
for i in range(n):
    a = input("請輸入學生的名字：")
    s = input("請輸入分數：")
    s = int(s)
    scores.append(s)
    if s < low:
        low = s
        lown = a
    if s > high:
        high = s
        highn = a
    total = s+total
    avg = total /n
print(scores)
print(low)
print(lown)
print(high)
print(highn)
print(avg)