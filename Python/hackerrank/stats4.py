N = int(input())
numbers = sorted([int(x) for x in input().split('+')])

def mean(numbs = []):
    return sum(numbs) / len(numbs) if len(numbs)!= 0 else None

# inbiased mean to calculate sample variance (n-1)
def unb_mean(numbs = []):
    return sum(numbs) / (len(numbs)-1) if len(numbs)!= 0 else None

print(numbers)
m = mean(numbers)
difs = [(x - m)**2 for x in numbers]
variance = unb_mean(difs)
print(variance)
std_dev = variance**.5
print(variance)
print("{0:0.1f}, {1:0.1f}".format(std_dev, variance))