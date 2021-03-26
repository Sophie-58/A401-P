def max_scores (a):
    max_ = 0
    for i in range(len(a)):
        if a[i] > a[max_]:
            max_ = i
    return max_
#-------------------------------
def min_scores (b):
    min_ = 0
    for o in range(len(b)):
        if b[o] < b[min_]:
            min_ = o
    return min_
#-------------------------------
def average (c):
    avg_ = 1
    for u in range(len(c)):
        avg_ = (l[0] + l[1] + l[2]) /3 
    return avg_

l = [10,20,30]

print(l[max_scores(l)])
print(l[min_scores(l)])
print(average(l))
