class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        count=10
        current=9
        for i in range(2,min(n,10)+1):
            current*=(11-i)
            count+=current
        return count
