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
    print(f"entering the info for row number: {x+1}")
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

print(f"startpoints {startpoints}")
def up(tup): # this works 
    if tup[0]-1<0: return None
    p=search[tup[0]-1]
    return p[tup[1]]  

def down(tup): # this works
    if tup[0]-1<0: return None
    p=search[tup[0]+1]
    print(f"x {p[tup[1]]} |||| y {tup[0]+1}")
    return p[tup[1]]  

def left(tup): # this works
    if tup[0]-1<0: return None
    p=search[tup[0]]
    try: return p[tup[1]-1]
    except IndexError: return None

def right(tup): # this works
    p=search[tup[0]]
    try: return p[tup[1]+1]  
    except IndexError: return None

def updiagl(tup): #this works
    if tup[1]-1 <0: return None
    if tup[0]-1 <0: return None
    try: return search[tup[0]-1][tup[1]-1]
    except IndexError: return None

def updiagr(tup): # this works
    if tup[1]+1 <0: return None
    if tup[0]-1 <0: return None
    try: return search[tup[0]-1][tup[1]+1]
    except IndexError: return None

def downdiagr(tup): # this works
    if tup[1]+1 <0: return None
    if tup[0]+1 <0: return None
    try: return search[tup[0]+1][tup[1]+1]
    except IndexError: return None

def downdiagl(tup): # this works
    if tup[1]+1 <0: return None
    if tup[0]-1 <0: return None
    try: return search[tup[0]+1][tup[1]-1]
    except IndexError: return None

# print(f"updiagleft {updiagl((0,1))}")
# print(f"updiagright {updiagr((0,1))}")  Debugging here, ignore
# print(f"downdiagleft {downdiagl((1,1))}")
# print(f"downdiagright {downdiagr((1,1))}")


def attempt(cord): # cord is a SINGLE TUPLE of coordinates for the first letter
    found=False
    trails=[[],[],[],[],[],[],[],[]] 
    
    while found==False:
        for x in startpoints:
            for y in range(1,len(query)): # This function takes a step in each direction for X letters, X being the length of the query
                print("Started taking a step in each direction")
                trails[0].append(up(cord))
                trails[1].append(down(cord))
                trails[2].append(left(cord))
                trails[3].append(right(cord))
                trails[4].append(updiagl(cord))
                trails[5].append(updiagr(cord))
                trails[6].append(downdiagl(cord))
                trails[7].append(downdiagr(cord))
            
        found=True
    return trails


print(startpoints)
for i in startpoints: print(attempt(i))