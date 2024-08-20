"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows

        curr_row = 0
        down = False

        for char in s:
            rows[curr_row] += char

            if curr_row == 0 or curr_row == numRows - 1:
                down = not down

            curr_row += 1 if down else -1

        return ''.join(rows)


if __name__ == "__main__":
    solution = Solution()
    assert solution.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert solution.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'


