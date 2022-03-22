"""
File: score_book.py
Name: Jerry Huang
----------------------
This program shows all the 
dict method by implementing 
a score book.
"""

# This controls when to break the loop for user inputs
QUIT = ''


def main():
	"""
	This main method contains 3 methods that
	constructing a score book. d is passed by reference
	"""
	d = {}
	get_scores(d)
	check_score(d)
	print_scores(d)
	

def get_scores(d):
	"""
	: param d: (dict) an empty python dict 
	--------------------------------------
	This method puts key->value pairs in d
	"""
	print("Let's input some data!")
	while True:
		name = input('Your name: ')
		if name == QUIT:
			break
		score = int(input('Your score: '))
		d[name] = score


def check_score(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This checks if key in d
	"""
	print("Let's check the score!")
	while True:
		name_to_check = input('Name to check: ')
		if name_to_check in d:
			print(d[name_to_check])
		elif name_to_check == QUIT:
			break
		else:
			print(f'there is no {name_to_check} in it')


def print_scores(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This method prints out all the key-value pairs
	"""
	print('-----------------------')
	for name, score in d.items():
		print(name, '->', score)


if __name__ == '__main__':
	main()