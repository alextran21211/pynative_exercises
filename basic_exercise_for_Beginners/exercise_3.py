#Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display 
#characters that are present at an even index number.

#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

#User Input 
string = input("Enter the string:")
print("Original string is", string)

# Method 1: Using range and len
def even_index_in_string(string):
	print("Printing only even index chars:")
	even_chars = ""
	for index in range(len(string)):
		if index % 2 == 0:
			print(string[index])
			even_chars += string[index]
	return even_chars

#even_index_in_string(string)

# Method 2: Using range only
def even_index_in_string_2(string):
	print("Printing only even index chars:")
	even_chars = ""
	for index in range(0, len(string), 2):
		print(string[index])
	#Don't need to call return if execute function only
	#not print function

#even_index_in_string_2(string)

# Method 3: Using string slicing
def even_index_in_string_3(string):
	#string_to_list = list(string)
	#don't need to convert
	print("Printing only even index chars:")
	for index in string[0::2]:
		print(index)

even_index_in_string_3(string)

#Manual User Input
#even_index_in_string("pynative")
#user_input = even_index_in_string("pynative")
#print(user_input)

#Note: If we print the function user_input above. even_chars string 
#will be printed in the screen. 
#      And if we don't have return string or number. By default, 
#the value is "None" will be shown in Output
#	   If we don't print user_input, just run the function 
#even_index_in_string. It will be fine, nothing will be popped 
#up beside the result.

