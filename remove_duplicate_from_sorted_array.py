# from typing import List

# # nums = [0,0,1,1,1,2,2,3,3,4]
# # nums = [1,1,2]
# nums = [1,1,2] # in use cases that the numbers are all orderd with non duplicate we miss 1 in k .
# # in cause of a single number we miss k. 
# # the use cause of duplicates give us the right k . 
# class Solution:
#     @staticmethod
#     def move_to_left(nums,flag):
#         """
#         Move every element that is duplicate from the start until the end.
#         append "_" in the end of the list,
#         end of the list would be the first '_'.

#         """
        
#         for i in range(1,len(nums)):
#             if nums[i] == nums[i-1]:
#                 element = nums.pop(i)
#                 nums[i-1] = element
#                 nums.append('_')
#                 break
#             # We rised a flag,Because we got to the end the first _
#             if (nums[i] == '_'):
#                 flag = True # or False
#                 break
#         return nums,flag ,i
    
#     def removeDuplicates(self, nums: List[int]) -> int:
#         flag = False
#         k = 1 
#         # Use case of len =1 
#         if len(nums) == 1 :
#             print("the length of nums is 1.")
#             return k ,nums
        
#         for i in range(1,len(nums)):
#             print("calling the move to the left")
#             nums,flag ,k = self.move_to_left(nums,flag)
            
#             if flag == True:
#                 print("break becuase we raised a flag", flag)
#                 break
#         print("we return the k and nums from , function removeDuplicates")
#         print(flag)
#         if flag == True:
#             return k, nums
#         if flag == False:
#             return k+1, nums
            
# sol  = Solution()
# k, ans = sol.removeDuplicates(nums)
# print('ans', ans)
# print('k',k)

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
        # if not nums:
        #     return 0 

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