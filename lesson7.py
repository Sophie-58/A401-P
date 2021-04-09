import random
ran = random.Random
n1 = ["I", "You", "We"]
v = ["like", "hate", "love"]
n2 = ["dogs", "cats", "turtles"]
for i in range(3):
    n1s = random.choice([0,1,2])
    vs = random.choice([0,1,2])
    n2s = random.choice([0,1,2])
    print(n1[n1s], v[vs], n2[n2s],".")