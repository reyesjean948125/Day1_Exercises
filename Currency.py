while True:

		rate = float(input("Enter conversion rate: "))
		print("[1] Convert USD to PHP")
		print("[2] Convert PHP to USD")
		print("[0] Exit")
		options = float(input("Select currency you want to convert: "))
		# int 1, 2, 3
		# float 1.12, 2.0
		if options == 1:
			# convert usd to php
			amount = float(input("Enter amount in USD:"))
			value = amount*rate
			print("%f USD = %f PHP" % (amount, value))
		elif options == 2:
			# convert php to usd
			amount = float(input("Enter amount in PHP:"))
			value = amount/rate
			print("%f PHP = %f USD" % (amount, value))
		elif options == 0:
			print("Invalid Option")  