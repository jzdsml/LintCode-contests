class Solution:
    """
    @param d:  limit the number of developers that can be seated consecutively with employees of the same type
    @param t:  limit the number of testers that can be seated consecutively with employees of the same type
    @param queries: the queries of team size 
    @return: return the number of ways
    """
    def theNumberofWays(self, d, t, queries):
        N = max(queries)
        MOD = 10**9 + 7
        
        dpD = [1] + [0]*N # cnt ending with D
        dpT = [1] + [0]*N # cnt ending with T
        preD = [0, 1] # prefix sum of cnt ending with D
        preT = [0, 1] # prefix sum of cnt ending with T

        for i in range(1, N+1):
            dpD[i] = preT[i]
            dpT[i] = preD[i]
            if i >= t:
                dpT[i] -= preD[i-t+1]
            if i >= d:
                dpD[i] -= preT[i-d+1]
            preD.append((preD[-1]+dpD[i]) % MOD)
            preT.append((preT[-1]+dpT[i]) % MOD)
            
        return [(dpT[q]+dpD[q]) % MOD for q in queries]
