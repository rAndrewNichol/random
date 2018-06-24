# for i in xrange(1, 101):
# 	fizzbuzz = "{}{}".format(("fizz" if i%3==0 else ""),("buzz" if i%5==0 else ""))
# 	print (fizzbuzz if fizzbuzz else i)

for i in xrange(1, 101):
	print "{}{}".format(("fizz" if i%3==0 else ""),("buzz" if i%5==0 else "")) or i

# i=0;exec("print i%3/2*'fizz'+i%5/4*'buzz'or i+1;i+=1;"*100)