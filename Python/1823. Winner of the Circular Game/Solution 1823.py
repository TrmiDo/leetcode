def findTheWinner(self, n, k):
    #Making the cycle
    ret=[]
    for index in range(1,n+1):
        ret.append(index)
            #Making initial move variable. Because the index is 1 unit smaller than value, we need to move 1 less step
    move=k-1
    while len(ret)!=1:
        ret.pop(move)
                    #We subtract 1 here because after we pop the value from the list, our position is pushed forward. 
                    #Hence, we pretend to take one step back so that we can move normally
        move+=k-1
                    #When we complete the cycle, the mod calculates how many steps left after we finish the cycle
        move=move%len(ret)

    return ret[0]
