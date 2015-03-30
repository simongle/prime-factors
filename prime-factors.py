# I built this with Python version 2.7.8
# It takes user input and displays all of the number's prime factors. 
# It is an adaptation of a solution to a problem from ProjectEuler.net
#! usr/bin/python

# Checks if a number is prime
def is_prime(f):
	# Catches 2 as a prime, since it would fail other tests
	if f == 2:
		return True
	# Is it an even number?
	if f%2 == 0:
		return False
	# Is each bit of output for the binary version of this number 1?
	if not f & 1:
		return False
	# Starting with 3 up to the square root of the number (since that is the highest possible factor) 
	# check by increments of two for factors. 
	for x in range (3, int(f**0.5)+1, 2):
		if f % x == 0:
			return False
	# Give me some prime numbers!
	return True
def get_primes(x):
	# Create an empty array to hold the prime factors
	prime_factors = []
	# Iterate through possible factor range
	for number in range(2, x-1):
		# Check to see that its a prime number
		if is_prime(number):
			# Does it divide the number evenly, i.e. is it a factor?
			if x % number == 0:
				# If it does, add it to our array
				prime_factors.append(number)
	# Give me some prime factors!	
	return prime_factors
# Error handling to account for rogue input such as strings
while True:
	try:
		# If the input is a legit integer, display its prime factors
    		x = int(raw_input("Please enter a number: "))
    		print get_primes(x)
    		# End the while loop, and the program
    		break
	except ValueError:
			# Give user the option to quit if they enter a string
			if raw_input("That doesn't look like a number, want to try again? (y / n): ") == 'y':
    				print "try again"
    			else:
    				break 