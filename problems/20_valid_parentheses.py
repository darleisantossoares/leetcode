class Solution:
    def isValid(self, s: str) -> bool:
        expected = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in expected:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last_item = stack[-1]
                if expected[last_item] != c:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
