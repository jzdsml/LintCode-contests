class Solution:
    """
    @param k: the number of auction participants
    @return: the number of confusing numbers
    """
    def theConfusingNumbers(self, k):
        d = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        self.ans = 0
        
        def dfs(a, b):
            if not (1 <= int(a) <= k and 1 <= int(b) <= k):
                return
            if a != b and len(str(int(a))) == len(str(int(b))):
                self.ans += 1
            for ch in d:
                dfs(a + ch, d[ch] + b)

        for key, value in d.items():
            dfs(key, value)

        return self.ans
