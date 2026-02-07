from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #i=0
        #take len of old_list and make array of 0s called new_list with index[0] of old_list in index[0] 
            #for j in array
            #put index[0] of new_list + index[0+1] of old_list into index[0+1] of new_list
            #index++
            #print(i, j, old_list, new_list)
        #set old_list to new_list
        #return old_list

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            #print(nums)
        return nums

print(Solution().runningSum([1,2,3,4]))
    #[1,3,3,4]
    #[1,3,6,4]
    #[1,3,6,10]