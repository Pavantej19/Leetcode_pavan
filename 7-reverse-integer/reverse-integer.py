class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        d=0 
        s=""
        while(x!=0):
            d=x%10
            s+=str(d)
            x//=10
        result = sign * int(s or "0")
        if result < -(2**31) or result > 2**31 - 1:
             return 0
        return result