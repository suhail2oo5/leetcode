class Solution(object):
    def strStr(self, haystack, needle):
        flag=-1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        if(flag==0):
            return 0
        else:
            return -1
        