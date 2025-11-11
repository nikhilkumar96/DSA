from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        last_char = '#'
        ele_count = 1
        i = 0
        while i < len(chars):
            if chars[i] == last_char:
                ele_count += 1
                chars.pop(i)
            else:
                if ele_count > 1:
                    chars.insert(i, str(ele_count))
                i+=1

        chars.append(ele_count)
        return len(chars)


print(Solution().compress(["a","a","b","b","c","c","c"]))
# print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))








