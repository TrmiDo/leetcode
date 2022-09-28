def majorityElement(self, nums):
    #The thinking process here is that when we sort the list,
    #because the major is more than half, we just need to return the number that appear right at the index more than half. 
    #The value of the majority of number will always take more than half the place (^-^)
    nums.sort()
    majorpos=len(nums)//2
    return nums[majorpos]
