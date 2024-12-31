"""
    Start of program
    If there are multiple instances of a word it will find the first occuring incidence ONLY
    In this program, X and Y are flipped, so instead of X,Y the notation is Y,X
"""

global search
search=[]

rows=int(input("How many rows> "))
cols=int(input("How many columns> "))

for x in range(0,rows): # Filling up rows with data, then pushing them to the SEARCH list
    print(f"entering the info for row number: {x}")
    o=[]
    for p in range(0,cols):
        a=input("letter> ")
        o.append(a)
    search.append(o)


query=input("What word would you like to find? ")
query=list(query)

fs=query[0]

def get_2d_coords(lst,tgt):#lst is the search, tgt is the target as a string
    cod=[]
    for x in range(0,len(lst)):
        for p in range(0,len(lst[x])):
            if tgt==lst[x][p]: cod.append((x,p)) 
    return cod
     
startpoints = get_2d_coords(search, fs)
complete=False

def up(tup): # this works
    if tup[0]-1<0: return None
    p=search[tup[0]-1]
    return p[tup[1]]  # returning the letter that is above the given coordinate

def down(tup): # this works
    if tup[0]-1<0: return None
    p=search[tup[0]+1]
    return p[tup[1]]  # returning the letter that is above the given coordinate

def left(tup): 
    if tup[0]-1<0: return None
    p=search[tup[0]]
    try: return p[tup[1]-1]  # returning the letter that is above the given coordinate
    except IndexError: return None

def right(tup): 
    p=search[tup[0]]
    try: return p[tup[1]+1]   # returning the letter that is above the given coordinate
    except IndexError: return None

print(right((1,2)))

def attempt(func,c):#function is the name of said function, and c is the coordinate tuple
   # do the func the amount of times the word is long
    for i in range(0,len(query)):
        res=[]
        res.append(func(c))
        
            
              
    
