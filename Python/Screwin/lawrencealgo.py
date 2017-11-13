# Number of combinations of 5 cards from 1-13 that sum to 32

def sum_32(total, num_cards, cards_used):
    if num_cards == 5:
        if total == 32:
            return 1
        else:
            return 0
    count = 0
    for i in range(cards_used[-1],14):
        if i not in cards_used:
            count += sum_32(total + i, num_cards + 1, cards_used + [i])
    return count

print(sum_32(0,0,[0]))