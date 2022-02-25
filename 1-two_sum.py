from typing import List
from time import perf_counter_ns

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j]== target:
                    return [i,j]
        return None

    def betterTwoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in vals:
                return [ vals[diff],i]
            else:
                vals[val] = i
        return None


if __name__ == '__main__':
    nums = [1,3,4,5,8,10,144,1080]
    target = 1083
    s = Solution()
    tic1 = perf_counter_ns()
    print(s.twoSum(nums,target))
    toc1 = perf_counter_ns()
    tic2 = perf_counter_ns()
    print(s.betterTwoSum(nums,target))
    toc2 = perf_counter_ns()
    time1 = toc1-tic1
    time2 = toc2-tic2
    perc = (time1-time2)/time1
    print(f"time1_ns: {time1}, time2_ns: {time2}, %: {perc}")