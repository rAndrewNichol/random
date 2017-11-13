import sys

initial = float(input('Initial lone value: $'))

APR = float(input('Enter APR: %'))

compound = input('Enter "a" for compounding annually, "m" for compounding monthly: ')

if compound=='a' or compound=='m':
	years = int(input('Please enter number of years: '))
	if compound=='a':
		APR=(APR/100)+1
		payments=years
		numerator=initial*(APR**payments)
		denominator=1
		for x in range(1,payments):
			denominator=denominator+(APR**x)
		yearly=numerator/denominator
		print ('Your yearly payment will be $%.2f' % yearly)
		print ('Your total cost of loan, assuming these yearly payments, will equal $%.2f' % (yearly*payments))
	if compound=='m':
		payments=years*12
		APR=((APR/12)/100)+1
		numerator=initial*(APR**payments)
		denominator=1
		for x in range(1,payments):
			denominator=denominator+(APR**x)
		monthly=numerator/denominator	
		print ('Your monthly payment will be $%.2f' % monthly)
		print ('Your total cost of loan, assuming these monthly payments, will equal $%.2f' % (monthly*payments))
else:
	sys.exit("Error, exiting program...")

## add one time final payment and compounding daily and different compounding/payment schedule
## add error messaging all around