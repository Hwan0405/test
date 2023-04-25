password = 'a123456'
i = 0
j = 3
while i < 3:
	p = input('pass:')
	i += 1
	if p == password:
		print('login succesfully')
		break
	else:
		j -= 1
		print('login failed', ',', j, 'chances left')
#password 