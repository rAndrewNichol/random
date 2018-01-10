#bigram jaccard

s1 = 'the departmnet of statistics at uc berkeley'
s2 = 'university of california, berkeley, department of statistics'


def bigrammify(s):
    counts = {}
    for bi in [s[i]+s[i+1] for i in range(len(s)-1)]:
        if bi in counts:
            counts[bi] +=1
        else:
            counts[bi] = 1
    return counts

def jaccard(s1,s2):
    b1,b2 = bigrammify(s1),bigrammify(s2) 
    in_common, not_in_common = 0, 0
    for b in set(b1) & set(b2):
        in_common += min(b1[b], b2[b])
        not_in_common += abs(b1[b]-b2[b])
        print(b + " : ",b1[b],b2[b]) 
    for b in set(b1) - set(b2):
        not_in_common += b1[b]
    for b in set(b2) - set(b1):
        not_in_common += b2[b]
    return in_common, (in_common+not_in_common)

print(jaccard('dogs are nice and fun to play with','dog is nice'))
