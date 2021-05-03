import random,sys,time,copy,os

"""Initially, there is a grid with some cells which may be alive or dead. Our task to generate the next generation of cells based on the following rules:

Any live cell with fewer than two live neighbours dies, as if caused by under population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
Examples:
The ‘#’ represent an alive cell and the ‘ ’ represent a dead cell.

"""

status={0:' ',1:'#'}  #we can use random int function to get random dead or alive
#check=lambda x: x=='#'  #truth checking function for alive but we instead use count()
f=lambda : random.randint(0,1)  #create random dead or alive

#func generates list of 8 possible neighbours, given argument tuple with two coordinates
getNeighbourIList=lambda *k: [(k[0]-1,k[1]-1),(k[0]-1,k[1]),(k[0]-1,k[1]+1),(k[0],k[1]-1),(k[0],k[1]+1),(k[0]+1,k[1]-1),(k[0]+1,k[1]),(k[0]+1,k[1]+1)]



def generateMatrix(h,w):
    status={0:' ',1:'#'}  #we can use random int function to get random dead or alive
    matrix=[]    #create empty matrix
    row=[]       #create empty row
    for i in range(h): #row major as we iterate through individual elements of each row
        for j in range(w):
            row.append(status[f()]) #randomly generated dead or alive 'w' no. of elements for each row 
        matrix.append(row)  #appending the above generated row into matrix for h times
        row=[]        #re-initialising empty row for next iteration
    return copy.deepcopy(matrix)

def updateMatrix(matrix):
    tempMatrix=[]
    alive=0
    h,w=len(matrix),len(matrix[0])
    tempRow=[]
    #filtering function for valid neighbours
    filterNeighbourI=lambda k: 1 if (k[0]>=0 and k[0]<h and k[1]>=0 and k[1]<w) else 0
    for rowIndex,row in enumerate(matrix):      #gives row index and list of elements in row
        for columnIndex,cell in enumerate(row):   #gives individual elements of each row with its column index
            count=0
            neighbours=[]            #initialise empty neighbour list
            #filter valid neighbours index and add those elements in neighbours list
            neighboursI=list(filter(filterNeighbourI,getNeighbourIList(rowIndex,columnIndex)))
            for l,k in neighboursI:
               # print(l,k,matrix[l][k], end='|') #for testing
                neighbours.append(matrix[l][k])
            #print('') #for testing
            count=neighbours.count('#')   #count for alive neighbours
            #print(rowIndex,columnIndex,count) #for testing

            #conditions for making or keeping element dead or alive in the new row
            if (cell==' ' and count==3) or (cell=='#' and (count==2 or count==3)):
                tempRow.append('#')
                alive+=1
            else:
                tempRow.append(' ')
            #print(tempRow)  #for testing
        tempMatrix.append(tempRow)   #add the new row in temp matrix
        tempRow=[]     #re initialise for new row
    
    return copy.deepcopy(tempMatrix) if alive else print("Matrix Dead")

def displayCells(matrix):
    print('-'*30)
    for row in matrix:  #prints the matrix
        print(row)


h=3 #height or no. of rows of dead-alive matrix
w=3 #width or no. of columns of dead-alive matrix
matrix=generateMatrix(h, w)

while True:
        displayCells(matrix)
        matrix=updateMatrix(matrix)
        time.sleep(1)
        if matrix==None:
            break
        os.system("cls")


