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

for i in range(0,num): # iterating until all words are found
    query=input("What word would you like to find? ")
    query=query.lower()
    query=list(query)

    try: fs=query[0]
    except IndexError: print("It doesn't look like you entered anything...")

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
        if tup[0]+i <0: return None
        if tup[1]-i <0: return None
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

                dire = trails.index(p) #numerical direction in which the algorithim shall traverse in
                if dire==0:
                    dire="up"
                    lst=trails[0]

                elif dire==1:
                    dire='down'
                    lst=trails[1]

                elif dire==2:
                    dire='left'
                    lst=trails[2]

                elif dire==3:
                    dire='right'
                    lst=trails[3]

                elif dire==4:
                    dire='top left'
                    lst=trails[4]

                elif dire==5:
                    dire= 'top right'
                    lst=trails[5]

                elif dire==6:
                    dire= 'bottom left'
                    lst=trails[6]

                elif dire==7:
                    dire= 'bottom right'
                    lst=trails[7]


                print(f'Row {x[0]+1} item {x[1]+1} Go {dire}')
            found=False




# its only locating the first two letters because we are not changing X (the coord value in which Python goes in each direction)
# Go in each direction until the second letters are known, then slice the (query list)'s first two values and match the prediction and the slice.