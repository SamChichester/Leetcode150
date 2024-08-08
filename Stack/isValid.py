"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for char in s:
            if char in brackets:
                top = stack.pop() if stack else None
                if brackets[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()")
    assert solution.isValid("()[]{}")
    assert not(solution.isValid("(]"))
    assert solution.isValid("{[]}")
    assert not(solution.isValid("(("))
    assert not(solution.isValid("}("))
