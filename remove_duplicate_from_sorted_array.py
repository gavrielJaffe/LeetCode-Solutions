from typing import List
nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:

    @staticmethod
    def move_to_left(nums):
        
        for i in range(1,len(nums)):
            if (nums[i] == nums[i-1]) and not(nums[i] == '_'):
                # print(f'{nums[i]} == {nums[i-1]}')
                element = nums.pop(i)
                nums[i-1] = element
                nums.append('_')
                break
        return nums 
    
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            # Move to every element to the left by 1,all of them.
            nums = self.move_to_left(nums)
            
        return nums
       
    
sol  = Solution()
ans= sol.removeDuplicates(nums)
print('', )
print('ans', ans)