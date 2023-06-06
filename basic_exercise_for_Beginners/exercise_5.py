#Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a 
#given list is same. If numbers are different then return False.

def check_first_last_number(list):
	if list[0] == list[-1]:
		return True
	return False 

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(check_first_last_number(numbers_x))
print(check_first_last_number(numbers_y))