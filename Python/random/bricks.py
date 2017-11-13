# def make_bricks(small,big,total):
# 	if small >= 5:
# 		big += small / 5
# 		small = small % 5	
# 	if total % 5 <= small and total / 5 <= big:
# 		return True
# 	return False
# print make_bricks(12,1,9)

# make_bricks = lambda small,big, total: total %5 <= small and total/5 <=big
# print make_bricks(3,1,9)

from fractions import Fraction
def make_bricks(small, big, goal, small_size, big_size):
	small, big, big_size, small_size = small*small_size, big*small_size, Fraction(big_size,small_size), 1
	return goal <= small + big*big_size and goal%big_size <= small

print make_bricks(4,2,16, 2, 4)