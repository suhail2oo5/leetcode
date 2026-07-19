class Solution(object):
    def twoSum(self, nums, target):
        x = {}
        for i, num in enumerate(nums):
            y = target - num
            if y in x:
                return [x[y], i]
            x[num] = i