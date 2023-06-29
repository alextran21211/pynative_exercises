#Exercise 8: Print the following pattern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

def print_pattern(number):
	for num in range(number):
		for i in range(num):
			print(num, end=" ")
		print("\n")

print_pattern(6)