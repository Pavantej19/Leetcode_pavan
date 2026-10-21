class Solution(object):
    def isValid(self, s):
        stack = []
        pair = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in pair:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_open_bracket = stack.pop()
                if pair[last_open_bracket] != char:
                    return False
        return not stack
sol=Solution()
sol.isValid("()")
        