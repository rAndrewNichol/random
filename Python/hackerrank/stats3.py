# Quartiles

N = int(input())
numbers = [int(x) for x in input().split()]
numbers = sorted(numbers)

# Could get from math.ceil() but fuck it. ALSO NEVER REALLY NEEDED THIS, can just do floor + 1.
# floor can also be found using integer division operator "//"
def ceiling(value = 0):
    if float(value) == 0:
        return 0
    elif int(float(value)) == 0:
        return 1
# if value is already an integer (int(float()) will take the floor of any value, even if in string format)
    if float(value)/int(float(value)) == 1:
        return value
    else: return int(float(value))+1

def median(numbs = [], N = 1):
    if N % 2 == 1:
        median = numbs[int(N/2)]
    else:
        median = (numbs[int(N/2 - 1)] + numbs[int(N/2)]) / 2
    return median

def q1(numbs = [], N = 1):
    return median(numbers[:int(N/2)], int(N/2))


def q3(numbs = [], N = 1):
    if N%2 ==1:
        return median(numbers[int(N/2)+1:], int(N/2))
    else: return median(numbers[int(N/2):], int(N/2))

# For some reason, hankerrank wants output as integers... :/
if N%2 == 1:
    print(int(median(numbers[:int(N/2)], int(N/2))))
    print(int(median(numbers, N)))
    print(int(median(numbers[int(N/2)+1:], int(N/2))))
else:
    print(int(median(numbers[:int(N/2)], int(N/2))))
    print(int(median(numbers, N)))
    print(int(median(numbers[int(N/2):], int(N/2))))
