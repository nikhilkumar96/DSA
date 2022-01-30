"""

https://www.geeksforgeeks.org/wildcard-character-matching/

Given two strings where first string may contain wild card characters and second string is a normal string. Write a
function that returns true if the two strings match. The following are allowed wild card characters in first string.

* --> Matches with 1 or more instances of any character or set of characters.

"""


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    last = 0
    flag = True
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
            if flag:
                last = i - 1
                flag = False

        if j == M:
            print("Found pattern at index", str(last))
            j = lps[j - 1]
            last = i - j
            flag = True
        elif pat[j] == '*':
            if j + 1 < M:
                if i + 1 >= N:
                    break
                if pat[j + 1] == txt[i + 1]:
                    j += 1
                i += 1
            else:
                print("Found pattern at index", str(last))
                j = lps[j]
                last = i - j
                flag = True

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
                last = i - j
                flag = True
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


txt = "ABABDABACDABABCABAB"
pat = "A*B"
KMPSearch(pat, txt)
