class Solution:
    """
    @param circles: The value of 6 points on n rings
    @return: Whether there are two same circles
    """
    def samecircle(self, circles):
        seen = set()
        for c0 in circles:
            c1 = tuple(sorted(c0))
            if c1 in seen:
                return True
            seen.add(c1)
        return False
