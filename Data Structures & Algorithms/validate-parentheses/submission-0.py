class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ")":"(", "]": "[", "}":"{"}

        for char in s:
            if char in "([{":
                stack.append(char)

            elif len(stack) == 0:
                return False

            elif stack[-1] != pairs[char]:
                return False

            else:
                stack.pop()

        return len(stack) == 0
        