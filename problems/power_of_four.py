from bisect import bisect_left


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        powers = [1 << p for p in range(0, 32, 2)]
        # for power in powers:
        #     if num == power:
        #         return True
        # return False
        pos = bisect_left(powers, num)
        return pos < len(powers) and powers[pos] == num


class SolutionTwo:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        bin_rep = bin(num)[2:]
        return bin_rep.count("1") == 1 and bin_rep.count("0") % 2 == 0


class SolutionThree:
    # num & (num - 1) unsets the least significant set bit
    # if it's 0, then it means there is only one 1
    # so it's a power of 2
    def isPowerOfFour(self, num: int) -> bool:
        # return num > 0 and num & (num - 1) == 0 and num == num & 0x55555555
        return num > 0 and num & (num - 1) == 0 and num & 0xAAAAAAAA == 0


class SolutionFour:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0
