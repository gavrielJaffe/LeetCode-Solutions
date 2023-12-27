from typing import List

nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]

class Solution:
    @staticmethod
    def move_to_left(nums,flag):
        """
        Move every element that is duplicate from the start until the end.
        append "_" in the end of the list,
        end of the list would be the first '_'.

        """

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                element = nums.pop(i)
                nums[i-1] = element
                nums.append('_')
                break
            # We rised a flag,Because we got to the end the first _
            if (nums[i] == '_'):
                flag = True # or False
                break
        return nums,flag ,i
    
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = False
        for i in range(1,len(nums)):
            nums,flag ,k = self.move_to_left(nums,flag)
            
            if flag == True:
                print("break becuase we raised a flag", flag)
                break
        return k, nums
    
sol  = Solution()
k, ans = sol.removeDuplicates(nums)
print('ans', ans)
print('k', type(k))
