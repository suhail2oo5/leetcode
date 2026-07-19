class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            a = 0
            while num > 0:
                a += num % 10
                num //= 10
            num = a
        return num