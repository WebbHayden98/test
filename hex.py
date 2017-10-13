while True:
	try:
		useri = input("Enter a hex digit: ")
		if 0 <= (useri) <= 9:
			print '{0:04b}'.format(useri)
			break
		else:
			print "Input is invalid."
	except NameError:
		useri = raw_input("Enter a hex digit: ")
		if useri == 'A':
			print '{0:04b}'.format(10)
			break
		elif useri == 'B':
			print '{0:04b}'.format(11)
			break
		elif useri == 'C':
			print '{0:04b}'.format(12)
			break
		elif useri == 'E':
			print '{0:04b}'.format(13)
			break
		elif useri == 'D':
			print '{0:04b}'.format(14)
			break
		elif useri ==  'F':
			print '{0:04b}'.format(15)
			break
		else:
			print "Input is invalid."