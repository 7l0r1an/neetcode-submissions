class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranteze = {')': '(', ']':'[', '}':'{'}
        for char in s:
            if char in paranteze:
                if not stack or stack[-1] != paranteze[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack)==0