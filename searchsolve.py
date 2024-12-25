# Start of program

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

def get_2d_coords(lst,tgt):
    cod=[]
    for x in range(0,len(lst)):
        for p in range(0,len(lst[x])):
            if tgt==lst[x][p]: cod.append((x,p)) 
    return cod

startpoints = get_2d_coords(search, fs)
print(startpoints)
complete=False

def up(cds): # cds is the tuple of coordinates
    print(tuple(cds[0]-1,cds[1]))
    return tuple(cds[0]-1,cds[1])

for i in range(0,len(startpoints)):
    up(startpoints[i])


# while complete != True:
#    # try each direction listed in my notes
#    pass #for now 

