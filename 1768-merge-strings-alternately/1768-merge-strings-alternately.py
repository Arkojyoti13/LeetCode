class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        max_len = max(len1, len2)
        merged = ""
        for i in range(max_len):
            if i < len1:
                merged+=word1[i]
            if i < len2:
                merged+=word2[i]
        return merged