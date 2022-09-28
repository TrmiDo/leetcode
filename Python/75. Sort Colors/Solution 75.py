def sortColors(self, nums):
    #Making a loop to find the smallest element to put on the "top of the list
    for last in range(len(nums)-1):
            #We start from the bottom
        start=len(nums)-1
        while start>last:
                    #Then we move up 1 at a time. if our current element is smaller than the one on top then we switch
            if nums[start]<nums[start-1]:
                temp=nums[start]
                nums[start]=nums[start-1]
                nums[start-1]=temp
            start-=1
         #After the the loop is complete. whatever element is on top is the Smallest so we dont have to go through it again. we just have to start from the bottom and go to the one semi-top.
                       
