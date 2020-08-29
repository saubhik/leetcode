# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
from random import randint


def rand7():
    return randint(1, 7)


# class Solution:
#     # abs(randint(1, 7) -  randint(1, 7)) is in [0, 6]
#     # Need [0, 3].
#     # int(abs(randint(1, 7) - randint(1, 7)) / 2) is in [0, 3]
#     # 0/2=0, 1/2=0, 2/2=1, 3/2=1, 4/2=2, 5/2=2, 6/2=3
#     # 3 has less probability of happening, so it is not uniform, but it is random.
#     def rand10(self):
#         return int(abs(rand7() - rand7()) / 2) + rand7()


class Solution:
    def rand10(self):
        while True:
            i, j = rand7(), rand7()
            idx = (i - 1) * 7 + j
            if idx < 41:
                return 1 + (idx - 1) % 10


class SolutionTwo:
    def rand10(self):
        while True:
            i, j = rand7(), rand7()
            idx = (i - 1) * 7 + j
            if idx < 41:
                return 1 + (idx - 1) % 10

            i, j = idx - 40, rand7()
            # i is in 1 to 9
            idx = (i - 1) * 7 + j
            if idx < 61:
                return 1 + (idx - 1) % 10

            i, j = idx - 60, rand7()
            # i is in 1 to 3
            idx = (i - 1) * 7 + j
            if idx < 20:
                return 1 + (idx - 1) % 10
