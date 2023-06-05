#Calculate the multiplication and sum of two numbers
#Given two integer numbers return their product only if 
#the product is equal to or lower than 1000, else return their sum.

def multiplication(number1, number2):
	if (number1 * number2) > 1000:
		return number1 + number2
	else:
		return number1 * number2

print("The result is", multiplication(20, 30))
print("The result is", multiplication(40, 30))
