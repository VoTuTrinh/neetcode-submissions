class Solution:
    def isPalindrome(self, s: str) -> bool:
        backward = ""
        forward = ""
        n = len(s)
        for i in range(0, len(s)):
            if('a' <= s[i].lower() <= 'z' or '0' <= s[i].lower() <= '9'):
                forward = forward + s[i].lower()

            if('a' <= s[n - 1 - i].lower() <= 'z' or '0' <= s[n - 1 - i].lower() <= '9'):
                backward = backward + s[n - 1 - i].lower()

        return backward == forward