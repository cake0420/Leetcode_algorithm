import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        s = re.sub('[^a-z0-9]','',s)
        print(s)
        return (s == s[::-1])