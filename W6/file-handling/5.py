#Write a Python program to write a list to a file.

items = ["1", "2", "3", "4", "5"]
file = open('sample.txt','w')
for item in items:
	file.write(item+"\n")
file.close()