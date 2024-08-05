# Single Number ( leetcode 136 )
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for x in nums:
            res^=x
        return res

---------------------------------------------------------
INPUT :- nums=[2,2,1] 
OUTPUT :-1
INPUT :- nums=[1]
OUTPUT :- 1
