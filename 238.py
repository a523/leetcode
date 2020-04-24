"""
238. 除自身以外数组的乘积
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
https://leetcode-cn.com/problems/product-of-array-except-self/
"""

nums = [1, 2, 3, 4]


# 方法1
def productExceptSelf(nums):
    L = []
    R = []
    for i in range(len(nums)):
        if i == 0:
            L.append(1)
        else:
            L.append(L[i - 1] * nums[i - 1])
    j = 0
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            R.append(1)
        else:
            R.append(R[j - 1] * nums[i + 1])
        j += 0
    R.reverse()

    ans = []
    for i in range(len(nums)):
        ans.append(L[i] * R[i])

    return ans


print(productExceptSelf(nums))


#  官方题解
def productExceptSelf2(nums):
    length = len(nums)
    L, R, answer = [0] * length, [0] * length, [0] * length
    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i - 1] * L[i - 1]

    R[length - 1] = 1
    for i in range(length - 2, -1, -1):
        R[i] = nums[i + 1] * R[i + 1]

    for i in range(length):
        answer[i] = L[i] * R[i]

    return answer


# 方法二

def productExceptSelf3(nums):
    length = len(nums)
    L, answer = [0] * length, [0] * length
    L[0] = 1
    for i in range(1, length):
        L[i] = L[i-1] * nums[i-1]

    R = 1
    for i in range(length-1, -1, -1):
        answer[i] = R * L[i]
        R = R * nums[i]

    return answer
