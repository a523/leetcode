"""473. 火柴拼正方形"""

nums = [1, 1, 2, 2, 2]


# def makesquare(nums) -> bool:
#     sum_nums = sum(nums)
#     if sum_nums % 4:
#         return False
#     else:
#         side_size = sum_nums // 4
#         stack = []
#         equal_side = 0
#         for n in nums:
#             if n > side_size:
#                 return False
#             else:
#                 if n == side_size:
#                     equal_side += 1
#                     if equal_side > 4:
#                         return False
#                 stack.append(n)
#

def makesquare(nums):
    sum_arr = sum(nums)
    if sum_arr % 4 != 0:
        return False
    edge_size = sum_arr // 2
    n = len(nums)
    # all_state =


print(makesquare(nums))
