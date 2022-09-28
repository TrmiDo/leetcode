def generateMatrix(self, n):
    #Part 1 Creating an empty square 
    #First row filled because we know the value of it
    ret=[]
    for row in range(n):
        ret.append([])
        if row==0:
            for column in range(1,n+1):
                ret[row].append(column)
        else:
            for column in range(n):
                ret[row].append(0)
            #Locating the last place the number were filled
    curRow=0
    curCol=n-1
    
    #Part 2 Going throw the square in a spiral way (look at the illustration)
    sign=1
    index=n
            # We can see that there is a pattern to how the spiral square is made
            #It moves through column then row. 
            #If it moves in the column in positive direction, it will move in the negative direction for row . Vice versa
    for move in range(n-1,0,-1):
        for rowmove in range(move):
            index+=1
            curRow+=sign
            ret[curRow][curCol]=index
                    #the sign only change in midway
        sign*=-1
        for colmove in range(move):
            index+=1
            curCol+=sign
            ret[curRow][curCol]=index
    return ret
