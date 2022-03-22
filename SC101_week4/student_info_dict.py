"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info.
"""


# The file name of our target text file
FILE = 'students_info.txt'


def main():
	all_d = {}
	######################
	with open(FILE, 'r') as f:
		for line in f:
			info_lst = line.split()
			name = info_lst[0]
			age = info_lst[1]
			email = info_lst[2]
			food = info_lst[3:]
			d_student = {'AGE': age, 'EMAIL': email, 'FOOD': food}

			# d_student = {}
			# d_student['AGE'] = age
			# d_student['EMAIL'] = email
			# d_student['FOOD'] = food
			all_d[name] = d_student
	######################
	print_out_d(all_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is the name of student
				value of type dict is the info of the student
	---------------------------------------------------------------
	This method prints out a nested data structure on console
	"""
	for student, student_d in d.items():
		print(student)
		print(student_d)
		print('-------------------------')


if __name__ == '__main__':
	main()
