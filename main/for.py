# Remove Element (leetcode 27)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index

---------------------------------------------------------------------------------
INPUT :- nums = [3,2,2,3] , val = 3
OUTPUT :- [2,2]
INPUT :- nums = [0,1,2,2,3,0,4,2] , val = 2
OUTPUT:- [0,1,3,0,4]
