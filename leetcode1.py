
# from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         big_list = []
#         print('nums', nums)
#         for i in range(len(nums)):
#             validate_list = [] 
            
#             for j in range(len(nums)):
#                 # print('j', j)
#                 # print('nums[j]', nums[j])
                
#                 if not i == j:
#                     validate_list.append(nums[j])
#                     if len(validate_list)+1 == len(nums):
#                         big_list.append(validate_list)
#         # print('big_list', big_list)
#         # print('nums', nums)
#         for i in range(len(big_list)):
#             # print('nums[i]', nums[i]) # 2,7,11,15
#             # print('i', i)
#             # print('big_list[i]', big_list[i])
#             for j in range(len(big_list[i])):
#                 # print('big_list[i][j]', big_list[i][j])
#                 # print('nums[i]', nums[i]) # 2,7,11,15
#                 if nums[i]+big_list[i][j] == target:
#                     # print('big_list[i][j]', big_list[i][j]) 
#                     ##
#                     """ 
#                     if we have the same index , we need to find the index  afterworrd  0,0 -> 0,2 
#                     """
#                     ##          0 1 2 
#                     # mylist = [3,2,3]
#                     item = big_list[i][j]
#                     start=i+1
#                     end=len(nums)
#                     # print('start', start)
#                     # print('end', end)
#                     #search for the item
#                     index = nums.index(item, start, end)
#                     print(f"index of {item} in the list : {index}")
#                     print(f'There is numbers that could add up to target {nums[i]} + {big_list[i][j]} = {target}')
#                     print(f'location: {index},{i}')
#                     # print('big_list[i][j]',type(big_list[i][j]))
#                     # print('big_list[i][j]',(big_list[i][j]))
                    
#                     return[i,index]
                
# sol = Solution()
# answer = sol.twoSum(nums,target=19999)
# print('answer',answer)




from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsList = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in numsList:
                return [numsList[diff], i]
            else:
                numsList[n] = i
# Test the function
sol = Solution()
nums = [2,4,6,8]
target = 10
answer = sol.twoSum(nums, target)
print(answer)  # Output should be [0, 1] because nums[0] + nums[1] = 2 + 7 = 9



# num_to_index = {}  # Create an empty dictionary

# # Suppose you have a list of numbers
# nums = [2, 7, 11, 15]

# # You can iterate through the list and store each number along with its index in the dictionary
# for i, num in enumerate(nums):
#     num_to_index[num] = i

# # Now, you can access the index of a number using its value as the key
# print(num_to_index[7])  # This will print 1, because the number 7 is at index 1 in the original list
# print(num_to_index[11])  # This will print 2, because the number 11 is at index 2
