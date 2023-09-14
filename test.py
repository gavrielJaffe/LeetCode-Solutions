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

a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"

answer = sol.addBinary(a, b)
print('answer:', answer)
