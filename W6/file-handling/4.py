#Write a Python program to count the number of lines in a text file.

def lines(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines:",lines("sample.txt"))