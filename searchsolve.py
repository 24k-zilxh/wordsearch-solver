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
query=query.lower()
query=list(query)

fs=query[0]

def get_2d_coords(lst,tgt):#lst is the search, tgt is the target as a string
    cod=[]
    for x in range(0,len(lst)):
        for p in range(0,len(lst[x])):
            if tgt==lst[x][p]: cod.append((x,p)) 
    return cod
     
startpoints = get_2d_coords(search, fs)

def up(tup,i): # this works, i is for loop iterator so we know how much to push off  
    if tup[0]-i<0: return None
    try: return search[tup[0]-i][tup[1]]
    except IndexError: return None  

def down(tup,i): # this works
    if tup[0]+i<0: return None
    try: return search[tup[0]+i][tup[1]]  
    except IndexError: return None
def left(tup,i): # this works
    if tup[0]-i<0: return None
    try: return search[tup[0]][tup[1]-i]
    except IndexError: return None

def right(tup,i): # this works
    try: return search[tup[0]][tup[1]+i]  
    except IndexError: return None

def updiagl(tup,i): #this works
    if tup[1]-i <0: return None
    if tup[0]-i <0: return None
    try: return search[tup[0]-i][tup[1]-i]
    except IndexError: return None

def updiagr(tup,i): # this works
    if tup[1]+i <0: return None
    if tup[0]-i <0: return None
    try: return search[tup[0]-i][tup[1]+i]
    except IndexError: return None

def downdiagr(tup,i): # this works
    if tup[1]+i <0: return None
    if tup[0]+i <0: return None
    try: return search[tup[0]+i][tup[1]+i]
    except IndexError: return None

def downdiagl(tup,i): # this works
    if tup[1]+i <0: return None
    if tup[0]-i <0: return None
    try: return search[tup[0]+i][tup[1]-i]
    except IndexError: return None


for x in startpoints: # iterating through each starting point, getting the first two letters in each dir
    
    trails=[[],[],[],[],[],[],[],[]] 
    for _ in trails:
        _.append(fs)
        
    for y in range(1,len(query)): # This function takes a step in each direction for the first 2 letters, then we know what direction to go in.
        trails[0].append(up(x,y)) # x,y is NOT The coordinates, X is the tuple and Y is the iterator
        trails[1].append(down(x,y))
        trails[2].append(left(x,y))
        trails[3].append(right(x,y))
        trails[4].append(updiagl(x,y))
        trails[5].append(updiagr(x,y))
        trails[6].append(downdiagl(x,y))
        trails[7].append(downdiagr(x,y))
    
    for p in trails:
                
        if p == query:
            
            dir = trails.index(p) #numerical direction in which the algorithim shall traverse in
            if dir==0:
                dir="up"
                lst=trails[0]
                
            elif dir==1:
                dir='down'
                lst=trails[1]
                          
            elif dir==2:
                dir='left'
                lst=trails[2]
                
            elif dir==3:
                dir='right'
                lst=trails[3]
              
            elif dir==4:
                dir='top left'
                lst=trails[4]
          
            elif dir==5:
                dir= 'top right'
                lst=trails[5]
           
            elif dir==6:
                dir= 'bottom left'
                lst=trails[6]
        
            elif dir==7:
                dir= 'bottom right'
                lst=trails[7]
            
            print(f'Start from coordinate {x} going {dir}')            
        
        found=False    
        

    
    
    
# its only locating the first two letters because we are not changing X (the coord value in which Python goes in each direction)
# Go in each direction until the second letters are known, then slice the (query list)'s first two values and match the prediction and the slice.
