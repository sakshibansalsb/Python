# Palindrome number 
  class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=x
        temp=0
        while n>0:
            temp=temp*10+n%10
            n//=10
        return temp==x
------------------------------------------------------------------
  INPUT: 10
  OUTPUT : False
  INPUT : 121
  OUTPUT: True
