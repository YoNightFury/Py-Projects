import random,sys,time,copy

"""Initially, there is a grid with some cells which may be alive or dead. Our task to generate the next generation of cells based on the following rules:

Any live cell with fewer than two live neighbors dies, as if caused by under population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Examples:
The ‘*’ represent an alive cell and the ‘.’ represent a dead cell.

"""

h=3 #height or no. of rows of dead-alive matrix
w=4 #width or no. of columns of dead-alive matrix

sts={0:' ',1:'#'}  #we can use random int function to get random dead or alive
ch=lambda x: x=='#'  #truth checking function for alive
f=lambda : random.randint(0,1)  #create random dead or alive

#func generates list of 8 possible neighbours, given argument tuple with two coordinates
nbil=lambda *k: [(k[0]-1,k[1]-1),(k[0]-1,k[1]),(k[0]-1,k[1]+1),(k[0],k[1]-1),(k[0],k[1]+1),(k[0]+1,k[1]-1),(k[0]+1,k[1]),(k[0]+1,k[1]+1)]
#filtering function for valid neighbours
nbf=lambda *k: 1 if (k[0][0]>=0 and k[0][0]<h and k[0][1]>=0 and k[0][1]<w) else 0

cells=[]    #create empty matrix
clm=[]       #create empty row
for i in range(h): #row major as we iterate through individual elements of each row
    for j in range(w):
        clm.append(sts[f()]) #randomly generated dead or alive 'w' no. of elements for each row 
    cells.append(clm)  #appending the above generated row into matrix for h times
    clm=[]        #re-initialising empty row for next iteration
for cl in cells:  #prints the matrix
    print(cl)
tcells=[]      #temporary matrix
tclm=[]         #temporary rows
for cli,cl in enumerate(cells):      #gives row index and list of elements in row
    for scli,scl in enumerate(cl):   #gives individual elements of each row with its column index
        cnt=0
        nbhs=[]            #initialise empty neighbour list
        #filter valid neighbours index and add those elements in nbhs list
        neighboursi=list(filter(nbf,nbil(cli,scli)))
        for l,k in neighboursi:
           # print(l,k,cells[l][k], end='|') #for testing
            nbhs.append(cells[l][k])
        #print('') #for testing
        cnt=nbhs.count('#')   #count for alive neighbours
        #print(cli,scli,cnt) #for testing

        #conditions for making or keeping element dead or alive in the new row
        if (scl==' ' and cnt==3) or (scl=='#' and (cnt==2 or cnt==3)):
            tclm.append('#')
        else:
            tclm.append(' ')
        #print(tclm)  #for testing
    tcells.append(tclm)   #add the new row in temp matrix
    tclm=[]     #re initialise for new row


print('-'*30)       
#display new matrix
for cl in tcells:
    print(cl)