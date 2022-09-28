class Solution(object):
def increasingTriplet(self, nums):
    #Setting up the marking point
    x,y=None,None
    for n in nums:
            #It is the safe to have the smallest element of the list to be the first element of the triplet because it has more possible larger value
        if n<=x or x==None:
            x=n
            #Yet, it is even safer to have the smallest pair because we only need one more larger element. 
        elif n<=y or y==None:
            y=n
            
            # For example, we have [20,30,10,...]
            # We know that we should keep track of  [20,30]. Yet we also need to keep track of 10
            #If the next number is 40, then we are done. Else, we can update our pair to a smaller one.
            #Although I said pair, we only need to keep track of the second number
        else:
            return True
    return False
