import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return x

        num = []
        places = math.log(x, 10)
        
        for i in range(1, places):
            num[i - 1] = (x % 10**i)

            if i > 1:
                num[i - 1] -= num[i - 2]

        reversed_num = []

        for val in num:
            reversed_num.insert(0, val)

        return reversed_num == num