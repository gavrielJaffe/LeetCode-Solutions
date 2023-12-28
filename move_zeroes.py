"""
take a list , and remove all of the zeros to the end . 
using the same list. 

"""

# def move_zeroes(nums):
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             zero = nums.pop(i)
#             nums.append(zero)
#     return nums

nums = [0,1,0,3,12,14]  # Output: [1,3,12,0,0]

def move_zeroes(nums):
    j = 0
    for i in range(1,len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j = j+1
    pos = get_max(nums)
    for i in range(pos+1,len(nums),1):
        nums[i] = 0
    return nums

def get_max(nums):
    max = nums[0]
    position = 0 
    for i in range(len(nums)):
        if nums[i] > max :
            max = nums[i]
            position = i
    return position
            
print(move_zeroes(nums))