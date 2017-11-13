def power(value, powr):
	print "value: {}, power: {}".format(value, powr)
	if powr == 0:
		return 1
	temp = power(value, powr/2)
	if powr % 2 == 0:
		return temp*temp
	else:
		return value * temp * temp

print power(2, 50)