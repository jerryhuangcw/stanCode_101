"""
File: factorial.py
Name:
--------------------------
This program shows what a recursion is by
implementing factorial function.
"""


def main():
	print(factorial(0))             # 1
	print(factorial(1))             # 1
	print(factorial(5))             # 120
	print(factorial(10))            # 3628800


def factorial(n):
	if n == 0:
		return 1
	else:
		ans = n*factorial(n-1)
		return ans


if __name__ == '__main__':
	main()