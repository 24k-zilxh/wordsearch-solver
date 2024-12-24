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
    for row in lst:
        cx=lst.index(row)
        for cell in row:
            cy=row.index(cell)
            if cell==tgt: cod.append([cx,cy])
            else: pass
    return cod

print(get_2d_coords(search,fs))

print("\n\n___________________________________________________________")
for popo in search:
    print(popo)