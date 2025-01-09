"""
    Start of program
    If there are multiple instances of a word it will find the first occuring incidence ONLY
    In this program, X and Y are flipped, so instead of X,Y the notation is Y,X
"""

global search
search=[]

rows=int(input("How many rows> "))
cols=int(input("How many columns> "))
num=int(input("how many words: "))

for x in range(0,rows): # Filling up rows with data, then pushing them to the SEARCH list
    print(f"entering the info for row number: {x+1}")
    o=input("Enter all characters from the line in one str>> ")
    o=list(o)

    search.append(o)


# its only locating the first two letters because we are not changing X (the coord value in which Python goes in each direction)
# Go in each direction until the second letters are known, then slice the (query list)'s first two values and match the prediction and the slice.