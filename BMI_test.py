h = float(input("please input height:"))
w = float(input("please input weight:"))
h = h / 100 # turn into m
bmi = w / (h**2)

if bmi < 18.5:
	print("your BMI :", bmi, "underweight")
elif bmi >= 18.5 and bmi < 24:
	print("your BMI :", bmi, "within the normal range")
elif bmi >= 24 and bmi < 27:
	print("your BMI :", bmi, "slightly heavier")
elif bmi >= 27 and bmi < 30:
	print("your BMI :", bmi, "mildly obesey")	
elif bmi >= 30 and bmi < 35:
    print('你的bmi值為', bmi, 'Moderate obesity')
elif bmi >= 35: # or else:
    print('你的bmi值為', bmi, 'severe obesity')