#Return the count of a given substring from a string
#Write a program to find how many times substring “Emma” appears in 
#the given string.

#str_x = "Emma is good developer. Emma is a writer"

#with string method count 
def count_substring(string, substring):
	x = string.count(substring)
	return x

string1 = "Emma is good developer. Emma is a writer. Emma comes from Brazil"
string2 = "Emma"

times = count_substring(string1, string2)
print(f"{string2} appeared {times} times")

#without string method
def count_substring2(string, substring):
	count = 0
	for i in range(len(string) - 1):
	#ensure that the loop iterates only up to the second-to-last 
	#character of the string.
		count += string[i:i+4] == substring
	return count

times2 = count_substring2(string1, string2)
print("Emma appeared", times2, "times")


