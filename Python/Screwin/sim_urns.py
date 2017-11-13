import random

# 0 = red
# 1 = black
urn1 = [0,0,0,0,1,1,1]
urn2 = [0,0,0,0,0,1,1,1,1]
urn3 = [0,0,0,0,1,1,1,1]
urns = [urn1,urn2,urn3]

draws = []
for x in range(100000):
    draw = []
    for i in range(3):
        draw.append(random.choice(urns[i]))
    draws.append(draw)

count = 0
for y in draws:
    if sum(y) == 1:
        count += 1
print(count)
print(count/100000)

