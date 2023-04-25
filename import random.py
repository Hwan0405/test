import random

r = random.randint(1, 100)

while True:
	n = int(input("guess a number:"))
	if n == r :
		print("guess right!")
		break
	elif n < r :
		print("is smaller than the answer")
	elif n > r :
		print("is bigger than the answer")


