# Maximum Subarray (leetcode 53)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            sum=max(sum+nums[i],nums[i])
            maxsum=max(sum,maxsum)
        return maxsum

------------------------------------------------
INPUT :- nums = [-2,1,-3,4,-1,2,1,-5,4]
OUTPUT : - 6
INPUT :- nums = [5,4,-1,7,8]
OUTPUT :- 23
