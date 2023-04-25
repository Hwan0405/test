password = 'a123456'
i = 3
while i > 0:
	p = input('pass:')
	i -= 1
	if p == password:
		print('login succesfully')
		break
	else:
		print('login failed', ',', i, 'chances left')
#password 