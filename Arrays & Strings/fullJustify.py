"""

Given an array of strings words and a width maxWidth, format the text such that each line has exactly
maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a
line does not divide evenly between words, the empty slots on the left will be assigned more spaces
than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified = []
        current = []
        count = 0

        for word in words:
            if count + len(word) + len(current) > maxWidth:
                for i in range(maxWidth - count):
                    current[i % (len(current) - 1 or 1)] += ' '
                justified.append(''.join(current))
                current = []
                count = 0

            current.append(word)
            count += len(word)

        justified.append(' '.join(current).ljust(maxWidth))
        return justified


if __name__ == "__main__":
    solution = Solution()
    assert solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
    assert solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16) == [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
