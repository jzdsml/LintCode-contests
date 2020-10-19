class Solution:
    """
    @param s: a string
    @return: a string
    """
    def largestLetter(self, s):
        setS = set(s)
        ans = "NO"
        for ch in setS:
            if ch.lower() in setS and ch.upper() in setS:
                if ans == "NO":
                    ans = ch.upper()
                else:
                    ans = max(ans, ch.upper())
        return ans
