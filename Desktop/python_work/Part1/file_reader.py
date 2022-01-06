##Reading sn entire file
with open('pi.txt') as file_object:
	contents = file_object.read()
print(contents.rstrip())

filename = 'pi.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

##Making a list of lines from a file
filename = 'pi.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())

##working with file contents
filename = 'pi.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))












