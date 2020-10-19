class Solution:
    """
    @param n: the number of members in team.
    @param groups: the groups.
    @return: return how many members will get notifications.
    """
    def teamNotification(self, n, groups):
        
        parents = list(range(n))
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
            
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parents[px] = py

        for group in groups:
            for i in range(1, len(group)):
                union(group[0], group[i])
        
        target = find(0)
        return sum(find(i) == target for i in parents)
