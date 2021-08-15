while True:
	num = int(input("Enter a number: "))

	if(num == 0 or num == 50 or num == -50):
		print("border")
	elif(num > 0 and num < 50):
		print("Positive range")
	elif(num < 0 and num > -50):
		print("Negative range")
	else:
		print("Out of range")