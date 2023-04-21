d = input("have you ever driven a car?")
if d != 'yes' and d != 'no' and d != 'no' and d != 'No':
	print('Please type yes or no')
	raise SystemExit

a = int(input("how old are you?"))
if d == 'yes' or d == 'Yes':
	if a >= 18 :
		print('okay, good!')
	else:
		print('Why did you ever drive??!')

elif d == 'no' or d == 'No':
	if a >= 18 :
		print('you can go to get a driving license now!')
	else:
		print("It's good, you can take a licence for a few year")
