
"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

链接：https://leetcode.cn/problems/two-sum

注意点：
1. 两个数为相同的数，如[3,3] target=6
2. 注意要在当前数值后查找如[3,4,2] target = 6

"""
class Solution:

    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        res = []
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                res.append(i)
                res.append(nums[i+1:].index(target-nums[i])+i+1)
        return res


    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if (target - num) in hashtable:
                return [i, hashtable[target - num]]
            hashtable[num] = i
