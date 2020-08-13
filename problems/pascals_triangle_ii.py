from typing import List


class Solution:
    # Binomial Coefficients:
    # nC0=1, nC1=n, n * (n-1)/2. n * (n-1)/2 * (n-2)/3
    #
    # Time: O(k)
    # Space: O(1) excluding result.
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        mid = int(rowIndex / 2)

        current_binomial_coefficient = 1
        for i in range(0, mid + 1):
            if i > 0:
                current_binomial_coefficient *= rowIndex - i + 1
                current_binomial_coefficient //= i
            result.append(current_binomial_coefficient)

        # it is symmetric
        if rowIndex > 0:
            if rowIndex % 2:
                result.extend(result[mid::-1])
            else:
                result.extend(result[mid - 1 :: -1])
        return result
