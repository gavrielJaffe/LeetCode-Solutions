
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed_number = ""
        for i in digits:
            reversed_number = str(i) + str(reversed_number)
        reversed_number = int(reversed_number[::-1]) +1 
        # Initialize a new list for the result
        digits = []
        reversed_number = str(reversed_number)
        for i in reversed_number:
            digits.append(int(i))
        return digits

sol = Solution()
answer = sol.plusOne([9])
print('answer', answer)