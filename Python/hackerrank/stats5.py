def median(numbs = [], N = 1):
    if N % 2 == 1:
        median = numbs[int(N/2)]
    else:
        median = (numbs[int(N/2 - 1)] + numbs[int(N/2)]) / 2
    return median

def q1(numbs = []):
    N = len(numbs)
    return median(numbs[:int(N/2)], int(N/2))


def q3(numbs = []):
    N = len(numbs)
    if N%2 ==1:
        return median(numbs[int(N/2)+1:], int(N/2))
    else: return median(numbs[int(N/2):], int(N/2))

# __main__
N = int(input())
numbers = [int(x) for x in input().split()]
freqs = [int(x) for x in input().split()]

filled = []
i = 0
for x in numbers:
    for r in range(freqs[i]):
        filled.append(x)
    i += 1

filled = sorted(filled)

print("{0:0.1f}".format(q3(filled) - q1(filled)))
