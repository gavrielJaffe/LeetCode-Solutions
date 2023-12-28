
# Accsepted  in Runtime 346 ms , Memory 18.84 mb
from typing import List
class Solution:
    @staticmethod
    def move_to_left(nums,flag):
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                element = nums.pop(i)
                nums[i-1] = element
                nums.append('_')
                break
            # We rised a flag,Because we got to the end the first _
            if (nums[i] == '_'):
                flag = True 
                break
        return nums,flag ,i
    
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = False
        k = 1 

        if len(nums) == 1 :
            return int(k)
        
        if len(nums) == 2 :
            if nums[0] == nums[1]:
                nums[1] = "_"
                return int(k)   
        
        if nums[0] == nums[-1]:
            for i in range(1,len(nums)):
                nums[i] =  "_"
            return 1        

        for i in range(1,len(nums)):
            nums,flag ,k = self.move_to_left(nums,flag)
            
            if flag == True:
                break

        if flag == True:
            # return k, nums
            return k
        if flag == False:
            # return k+1, nums
            return int(k+1)
            
sol  = Solution()
k = sol.removeDuplicates(nums = [1,1,2])
print(k)