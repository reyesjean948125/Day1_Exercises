while True: 
		P = int(input("Enter amount of loan: "))
		Y = int(input("Years to pay: "))
		R = float(input("Interest rate: "))

		n = 12*Y
		r = R/(12*100)

		payment = (P*r)/(1-((1+r)**-n))
		print("Payment for ", Y, " year/s is: ", payment)