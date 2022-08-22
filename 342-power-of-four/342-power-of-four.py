# Convert to binary, if the first element of the binary is 1 and all others 0 and len(bin(n)) is odd. return True
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        binN = bin(n)[2:]
        return (binN[0] == '1' and binN.count('1') == 1) and  len(binN) % 2 != 0