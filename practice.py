

#challange1 ##function which prints all of the primes to a number


def prim_finder(num):

	q_prim = True

	for i in range(2,num):
		if num%i == 0:
			q_prim = False

	return q_prim

def list_primes(digit):

	for i in range(3,digit):
		if prim_finder(i) == True:
			print(i)



#challange2#function which prints the factors of a number which are prime

def prim_factors(num):
	for i in range(2,num):
		if num%i == 0 and prim_finder(i) == True:
			print(i)


#challange3: find prime number, input from user for find next prime of to quit


initial_prime = 0
now_prime = 1
curr_pos = 1
keep_going = 'n'

print('\nThe first prime number is 1')

while True:
	
	keep_going = input('Would you like to know the next prime number? y/n\t')

	if keep_going == 'y':
		while True:
			curr_pos += 1
			if prim_finder(curr_pos) == True:
				break
		print(f'\nThe next prime number is {curr_pos}\n')

	elif keep_going == 'n':
		print('Thanks for playing\n')
		break

	else:
		print('Please input either a "y" or a "n" character\n')






