import struct
from typing import List
# 67 add_binary.py 

def binary_str_to_decimal(a):
    # convert from binary to int    
    binary_str = a

    # Convert binary string to integer
    binary_int = int(binary_str, 2)

    # Pack integer into binary string
    binary_pack = struct.pack('>I', binary_int)

    # Unpack binary string into integer
    decimal = struct.unpack('>i', binary_pack)[0]

    print('decimal', decimal)

    return decimal

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert from binary strings to int
        num_a = binary_str_to_decimal(a)
        num_b = binary_str_to_decimal(b)
        # Adding both of the decimal to sum
        sum = num_a + num_b
        # Convert sum to a binary, from int to binary
        return str(bin(sum))[2:]

sol = Solution()


a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"

answer = sol.addBinary(a,b)
print('answer:', answer)

    # 1010
    # 1011
   # 10101
