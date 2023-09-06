class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Test for negative numbers
        if x < 0 :
            return False
        x = str(x)
        half_size = len(x) / 2 
        half_size = int(half_size)
        # Test for evens
        if len(x) % 2 == 0 : 
            for i in range((half_size)):
                remainder = len(x)-1 - i 
                if x[i] == x[remainder]:
                    continue
                else:
                    return False
        # Test for odds
        elif (len(x) % 2) == 1 :
            for i in range((half_size)):
                remainder = len(x)-1 - i 
                if x[i] == x[remainder]:
                    print(f'comeper {x[i]}-{x[remainder]}')
                    continue
                else:
                    return False
        return True

x = 12421

sol = Solution()
answer = sol.isPalindrome(x)
print('answer',answer)
