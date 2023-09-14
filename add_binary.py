def binary_str_to_decimal(binary_str):
    # Convert binary string to integer
    decimal = int(binary_str, 2)
    return decimal

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to decimal integers
        num_a = binary_str_to_decimal(a)
        num_b = binary_str_to_decimal(b)
        # Perform addition
        result = num_a + num_b
        # Convert the result back to a binary string
        return bin(result)[2:]  # Removing the '0b' prefix

sol = Solution()

a = "1010"
b = "1011"

answer = sol.addBinary(a, b)
print('answer:', answer)
