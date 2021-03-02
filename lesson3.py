import random
ans = random.randint(1,10)
time = 0

while (time <= 4):
    b = input('input number:')
    b = int(b)
    if b < 0 or b > 10:
        print('錯誤數字')
    else:
        time = time+1
        if b==ans :
            print('猜對了，恭喜！')
            break
        else:
            if b > ans:
                print('太大囉！')
            elif b < ans:
                print('太小囉！')
            print('再猜一次')
if time >=4:
    print('真可惜，失敗了')
else:
    print('恭喜你，你總共用了',time,'次')