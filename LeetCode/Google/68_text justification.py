"""

https://leetcode.com/problems/text-justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

"""


class Solution:
    def fill_space(self, loc_res, maxi):
        while len(loc_res) < maxi:
            loc_res += ' '
        return loc_res

    def get_line(self, words, maxi, loc_sumi, last_line=False):
        loc_res = ""
        if last_line:
            for i in words:
                loc_res += i
                if len(loc_res) + 1 < maxi:
                    loc_res += ' '

            loc_res = self.fill_space(loc_res, maxi)
        else:
            tot_space_need = maxi - loc_sumi
            li = [1 for i in range(len(words))]
            if len(li) == 1:
                loc_res += words[0]
                loc_res = self.fill_space(loc_res, maxi)
            else:
                li[-1] = 0
                for i in range(tot_space_need):
                    li[i % (len(words) - 1)] += 1
                for i in range(len(words)):
                    loc_res += words[i]
                    for j in range(li[i]):
                        loc_res += ' '
        return loc_res

    def fullJustify(self, words, maxWidth: int):
        res = []
        loc_sumi = 0
        prev = 0
        i = 0
        while i < len(words):
            if loc_sumi + len(words[i]) <= maxWidth:
                loc_sumi += (len(words[i]) + 1)
            else:
                res.append(self.get_line(words[prev:i], maxWidth, loc_sumi - 1))
                prev = i
                loc_sumi = len(words[i])
                loc_sumi += 1
            i += 1
        res.append(self.get_line(words[prev:i], maxWidth, loc_sumi - 1, True))
        return res


print(Solution().fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"]
    , 20))


"""
Fastest Solution

def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        L = 0
        while L < len(words):
            R = L
            cumulativeChars = 0
            while R < len(words) and R-L+cumulativeChars+len(words[R]) <= maxWidth:
                cumulativeChars += len(words[R])
                R += 1
            if R == len(words) or R == L+1:
                # last line or one word line so left justify
                line = []
                for i in range(L, R):
                    line.append(words[i])
                    if i != R-1:
                        line.append(' ')
                line.append(' '*(maxWidth-cumulativeChars-R+L+1))
                lines.append(''.join(line))
            else:
                allSpaces, firstWords = divmod(maxWidth-cumulativeChars, R-L-1)
                line = []
                line.append(words[L])
                for i in range(L+1, R):
                    if firstWords > 0:
                        firstWords -= 1
                        line.append(' ')
                    line.append(' '*allSpaces)
                    line.append(words[i])
                lines.append(''.join(line))
            L = R
        return lines

"""