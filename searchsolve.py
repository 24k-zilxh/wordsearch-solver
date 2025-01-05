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

def up(tup): # this works 
    if tup[0]-1<0: return None
    try: return search[tup[0]-1][tup[1]]
    except IndexError: return None  

def down(tup): # this works
    if tup[0]+1<0: return None
    try: return search[tup[0]+1][tup[1]]  
    except IndexError: return None
def left(tup): # this works
    if tup[0]-1<0: return None
    try: return search[tup[0]][tup[1]-1]
    except IndexError: return None

def right(tup): # this works
    try: return search[tup[0]][tup[1]+1]  
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


for x in startpoints: # iterating through each starting point, getting the first two letters in each dir
    
    trails=[[],[],[],[],[],[],[],[]] 
    for _ in trails:
        _.append(fs)
        
    for y in range(0,1): # This function takes a step in each direction for the first 2 letters, then we know what direction to go in.
        trails[0].append(up(x))
        trails[1].append(down(x))
        trails[2].append(left(x))
        trails[3].append(right(x))
        trails[4].append(updiagl(x))
        trails[5].append(updiagr(x))
        trails[6].append(downdiagl(x))
        trails[7].append(downdiagr(x))
    
    for p in trails:
        print(f"is {p} equal to {query[:2]}")
        
        if p == query[:2]:
            
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
                dir='updiagl'
                lst=trails[4]
          
            elif dir==5:
                dir= 'updiagr'
                lst=trails[5]
           
            elif dir==6:
                dir= 'downdiagl'
                lst=trails[6]
        
            elif dir==7:
                dir= 'downdiagr'
                lst=trails[7]
            
                print(lst)
            print(dir)            
        
        found=False    
        

    
    
    
# its only locating the first two letters because we are not changing X (the coord value in which Python goes in each direction)
# Go in each direction until the second letters are known, then slice the (query list)'s first two values and match the prediction and the slice.
