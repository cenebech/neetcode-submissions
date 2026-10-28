class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        resut = 0

        while left <= right:
            mid = (left+right)//2
            square = mid * mid

            if square == x:
                return mid


            elif square < x:
                result = mid
                left = mid + 1

            elif square > x:
                right = mid - 1

        return result
        