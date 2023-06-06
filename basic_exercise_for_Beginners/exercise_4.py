#Remove first n characters from a string
#Write a program to remove characters from a string starting from zero 
#up to n and return a new string.

#For example:

#remove_chars("pynative", 4) so output must be tive. Here we need to 
#remove first four characters from a string.
#remove_chars("pynative", 2) so output must be native. Here we need to 
#remove first two characters from a string.
#Note: n must be less than the length of the string.

#Method 1: using slicing
def remove_chars(string, n):
	while n < len(string):
		removed_string = string[n:]
		return removed_string
	else:
		return ""

#Method 2: using del statement
#del statement only use for list type
#we need convert string to list 
#and then join list to string again
#complex method
def remove_chars_2(string, n):
	while n < len(string):
		string_to_list = list(string)
		del string_to_list[:n]
		list_to_string = ''.join(string_to_list)
		return list_to_string

#method 3: using pop() method
def remove_chars_3(string, n):
	while n < len(string):
		string_to_list = list(string)
		for index in range(n):
			string_to_list.pop(0)
		return ''.join(string_to_list)

#method 4: remove value from a list
#don't use this


print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
print(remove_chars("pynative", 3))

# print(remove_chars_2("pynative", 4))
# print(remove_chars_2("pynative", 2))
# print(remove_chars_2("pynative", 3))

# print(remove_chars_3("pynative", 4))
# print(remove_chars_3("pynative", 2))
# print(remove_chars_3("pynative", 3))

#Note:
#When we work with string. We should think about slicing first
#pop(), remove() or del statement using for list type
#string is immutable