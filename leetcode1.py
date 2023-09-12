from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        big_list = []
        for i in range(len(nums)):
            validate_list = [] 
            
            for j in range(len(nums)):
                # print('j', j)
                # print('nums[j]', nums[j])
                
                if not i == j:
                    validate_list.append(nums[j])
                    if len(validate_list)+1 == len(nums):
                        big_list.append(validate_list)
        # print('big_list', big_list)
        # print('nums', nums)
        for i in range(len(big_list)):
            # print('nums[i]', nums[i]) # 2,7,11,15
            # print('i', i)
            # print('big_list[i]', big_list[i])
            for j in range(len(big_list[i])):
                print('big_list[i][j]', big_list[i][j])
                print('nums[i]', nums[i]) # 2,7,11,15
                if nums[i]+big_list[i][j] == target:
                    # print('big_list[i][j]', big_list[i][j]) 
                    ##
                    """ 
                    if we have the same index , we need to find the index  afterworrd  0,0 -> 0,2 
                    """
                    ##          0 1 2 
                    # mylist = [3,2,3]
                    item = big_list[i][j]
                    start=i+1
                    end=len(nums)

                    print('start', start)
                    print('end', end)
                    #search for the item
                    index = nums.index(item, start, end)
                    print(f"index of {item} in the list : {index}")
                    print(f'There is numbers that could add up to target {nums[i]} + {big_list[i][j]} = {target}')
                    print(f'location: {index},{i}')
                    # print('big_list[i][j]',type(big_list[i][j]))
                    # print('big_list[i][j]',(big_list[i][j]))
                    
                    return[i,index]


                    


                
sol = Solution()
answer = sol.twoSum(nums=[3,2,3],target=6)
print('answer',answer)