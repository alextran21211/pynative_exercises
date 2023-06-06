#Print the sum of the current number and the previous number
#Write a program to iterate the first 10 numbers 
#and in each iteration, print the sum of the current and previous number.

#first method
# print("Printing current and previous number sum in range(10)")
# for number in range(10):
# 	if number == 0:
# 		print("Current number 0 Previous Number 0 Sum: 0")
# 	else:
# 		print("Current number {} Previous Number {} Sum: {}".
# 		format(number, number - 1, number + (number - 1)))

#second method (better)
print("Printing current and previous number sum in range(10)")
pre_num = 0
for number in range(10):
	print("Current number {} Previous Number {} Sum: {}".
	format(number, pre_num, number + pre_num))
	pre_num = number
	
