# for the random selection
from random import choice
# to create the sorted dictionary
import collections
 
 
# if throwDice() is called without param, assume that summed equals 0 
# used when player rolls a '6'
def throwDice(*args):
	if not args: 
		summed = 0
	else:
		summed = args[0]
	# roll the dice
	x = choice(range(1,7))
	# if '6' was rolled, we roll again until x <> 6 is rolled
	if x == 6:
		return throwDice(summed+6)	
	else:
	# if no '6' was rolled in *this* run, we just return the aggregated number	
		return summed+x
 
# little test function to get the absolute frequencies
def TestDice(n):
	# create a dictionary
	d = {}
	for x in range(0, n):
		# roll the dice
		wurf = throwDice()	
 
		# if key is found, just increase its frequency by 1 
		if wurf in d:
			d.update({wurf:d[wurf]+1})
		else:
			# else create new key with initiL frequency 1 
			d.update({wurf:1})
	od = collections.OrderedDict(sorted(d.items()))
	for k, v in od.iteritems(): 
		print(k, v)
 
TestDice(6000)