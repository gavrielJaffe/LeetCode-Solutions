#  Binary Search is O(log n)


# Example 1:
#                l     r 
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  # Subtract 1 to make sure it's a valid index
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ""



sol = Solution()


answer = sol.searchInsert(nums=[1,3,5,6],target=5)
print('answer', answer)