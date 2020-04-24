"""
15. 三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""


def threeSum(nums):
    n = len(nums)
    res = []
    if not nums or n < 3:
        return []
    nums.sort()
    for i in range(n):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        L = i + 1
        R = n - 1
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                

