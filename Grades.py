while True:

	grade = float(input("Enter grade: "))
	if (grade >= 90):
		print('A')
	elif (grade >= 80):
		print('B')
	elif (grade >= 70):
		print('C')
	elif (grade >= 60):
		print('D')
	elif (grade >= 0):
		print('E')
else:
    print('Invalid Number')