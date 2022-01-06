#Writing to a file
#an empty file

filename = 'programming.txt'
with open(filename, 'w') as file_object:
	file_object.write("I love programming.")

##store numerical data in a text file by converting into string data using str()
