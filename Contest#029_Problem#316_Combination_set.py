class Solution:
    """
    @param num: a array
    @param target: a num
    @return: return all combinations
    """
    
    def combinationSet(self, num, target):
        ans = []
        
        def dfs(i):
            if i < target:
                ans.append(i)
            else:
                return
            if i:
                for c in num:
                    dfs(i*10 + c)
                    
        for c in num:
            dfs(c)
        return ans

    # Another solution.
    def combinationSet2(self, num, target):
        num.sort()
        ans = set()
        for n in num:
            if n < target:
                ans.add(n)
            else:
                return list(ans)
        prev = set(ans)
        while True:
            prev = set(ans)
            for pre in prev:
                for n in num:
                    if 10*pre + n < target:
                        ans.add(10*pre + n)
                    else:
                        return list(ans)
                            
    # Another solution.
    def combinationSet3(self, num, target):
        ans, num = [], set(map(str, num))
        for i in range(target):
            if set(str(i)) <= num:
                ans.append(i)
        return ans
