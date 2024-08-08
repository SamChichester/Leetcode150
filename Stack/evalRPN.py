"""

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    if num1 * num2 < 0 and num1 % num2 != 0:
                        stack.append(num1 // num2 + 1)
                    else:
                        stack.append(num1 // num2)

            else:
                stack.append(int(token))

        return stack[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
