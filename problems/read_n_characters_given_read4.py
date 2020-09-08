"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


def read4(buf4):
    # just a dummy function to remove IDE complaints
    return 4


class Solution:
    # Time: O(n)
    # Space: O(1) space, to keep buffer of 4 characters every iteration.
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while True:
            buf4 = [""] * 4
            k = read4(buf4)
            if k == 0:
                break
            for j in range(k):
                if i >= n:
                    break
                buf[i] = buf4[j]
                i += 1
        buf = buf[:i]
        return i
