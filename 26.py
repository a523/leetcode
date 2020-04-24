"""26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""
nums = [0,0 ,1, 2,3,3,4]


def removeDuplicates(nums):
    tag = len(nums)
    for i in range(1, len(nums)):
        pre = nums[i - 1]
        if pre == nums[i]:
            if tag == len(nums):
                tag = i
        else:
            if tag != len(nums):
                nums[tag] = nums[i]
                tag += 1
    return tag


tag = removeDuplicates(nums)

print(nums[:tag])
