class Solution(object):
    def plusOne(self, digits):
        k=0
        for i in digits:
            k=k*10+i
        k=k+1
        return list(map(int, str(k)))
