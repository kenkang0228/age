x = input('Have you ever driven a car ?')
if x != 'Y' and x != 'N':
	print('You only input Y or N')
	raise SystemExit

y = input('How old are you ?')
y = int(y)
if x == 'Y':
	if y >= 20:
	    print('You Pass')
	else:
		print('WTF !?  Why you can drive ?') 
elif x == 'N':
	if y >= 20:
		print('You can take a driver license test.')
	else:
		print('Wait for you growing up to 20 years old.')