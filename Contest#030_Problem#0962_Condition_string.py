class Solution:
    """
    @param s: a string only contains `a-f`
    @return: The longest length that satisfies the condition
    """
    def conditionString(self, s):
        import bisect
        s1 = []
        s2 = []
        ch2val = {"a":1, "b":1, "c":2, "d":2, "e":3, "f":3}
        for ch in s:
            if ch in "ace":
                s1.append(ch2val[ch])
            else:
                s2.append(ch2val[ch])
        
        def LIS(s0):
            d = []
            for val in s0:
                idx = bisect.bisect_left(d, val + 1)
                if idx == len(d):
                    d.append(val)
                else:
                    d[idx] = val
            return len(d)
        
        return LIS(s1) + LIS(s2)
