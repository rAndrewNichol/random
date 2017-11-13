# Weighted Mean

N = int(input())
values = input().split()
weights = input().split()
weighted_values = []
for i in range(N):
    values[i] = int(values[i])
    weights[i] = int(weights[i])
    weighted_values.append(values[i]*weights[i])

weighted_mean = round(sum(weighted_values)/sum(weights),1)

print(weighted_mean)

# Input shortcut(works in executable and not in console)
# X = list(map(int, input().split()))

# short method:

n = int(input())
nums = [int(x) for x in input().split()]
weight = [int(x) for x in input().split()]
print (round(float(sum([nums[i]*weight[i] for i in range(n)]))/sum(weight), 1))
