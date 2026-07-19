class Solution(object):
    def lengthOfLastWord(self, s):
        a=s[::-1]
        c=0
        for i in range(len(a)):
            if(a[i]==" " and c==0):
                pass
            elif(a[i]==" "):
                break
            else:
                c+=1
        return c