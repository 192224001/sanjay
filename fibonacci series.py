def fibonacci(n):
	a = int(input("enter a number"))
	b = int(input("enter a number"))
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b
print(fibonacci(9))


