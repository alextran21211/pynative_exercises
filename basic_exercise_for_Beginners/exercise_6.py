#Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those 
#numbers which are divisible by 5

def numbers_divide_by_5(list):
	print(f'Given list is {list}')
	print('Divisible by 5')
	for num in list:
		if num % 5 == 0:
			print(num)

new_list = [10, 20, 33, 46, 55]
numbers_divide_by_5(new_list)





