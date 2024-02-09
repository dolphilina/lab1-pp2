"""Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set."""

def unique(dupl):
    newlist = []
    for n in dupl:
        if n not in newlist:
            newlist.append(n)
    return newlist
    
dupl = []
a = int(input())
for i in range(a):
    dupl.append(int(input()))

print(unique(dupl))