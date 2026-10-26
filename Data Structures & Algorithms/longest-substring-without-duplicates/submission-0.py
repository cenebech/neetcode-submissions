class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        This video helped me learn to solve this question

        # https://www.youtube.com/watch?v=FCbOzdHKW18&t=604s

        this is a sliding windows problem
        """

        seen = set()
        longest = 0
        left = 0

        for right in range (len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            window = (right - left) + 1
            longest = max(longest,window)

        return longest



        