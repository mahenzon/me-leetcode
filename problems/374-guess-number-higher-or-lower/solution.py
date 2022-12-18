# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while True:
            # middle = left + (right - left) // 2
            middle = (left + right) // 2
            wrong = guess(middle)
            if not wrong:
                return middle

            if wrong == 1:
                left = middle + 1
            else:
                right = middle - 1
