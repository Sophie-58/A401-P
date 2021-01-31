sm = input("請輸入數學成績：")
sE = input("請輸入英文成績：")
sm = int(sm)
sE = int(sE)
if  (sm>= 90)and(sE>= 90):
    print("有獎品")
elif (sm<= 60)and(sE<= 60):
    print("要處罰")
else:
    print("再加油")
# 9 and 10 可改為：elif (sm<= 60)or(sE<= 60):
    #print("再加油")