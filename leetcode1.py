from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] == target:
                return[i,i+1]


sol = Solution()
answer = sol.twoSum(nums=[3,2,3],target=6)
print('answer', answer)