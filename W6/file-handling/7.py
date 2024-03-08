#Write a Python program to copy the contents of a file to another file

with open("sample.txt") as f:
    with open("A.txt", "w") as f1:
        for line in f:
            f1.write(line)