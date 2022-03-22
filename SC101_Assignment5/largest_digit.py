"""
File: largest_digit.py
Name: Jerry Huang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

# global var:
max_digit = 0  # the current largest digit


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, input value
	:return: max_digit, largest digit in the input value
	"""
	global max_digit
	max_digit = 0  # reset max_digit
	helper(abs(n))  # get rid of negative sign
	return max_digit


def helper(num):
	"""
	Get each digit value by calculating the remainder of "num" divided by 10 recursively.
	"""
	global max_digit
	if num == 0:
		pass
	else:
		if num % 10 >= max_digit:
			max_digit = num % 10
			helper(num // 10)
		else:
			helper(num // 10)


if __name__ == '__main__':
	main()
