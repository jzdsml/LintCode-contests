class Solution:
    """
    @param E: the number of easy problems
    @param EM: the number of "easy and medium" problems
    @param M: the number of medium problems
    @param MH: the number of "medium and hard" problems
    @param H: the number of hard problems
    @return: nothing
    """
    def theNumberOfContests(self, E, EM, M, MH, H):
        
        def valid(guess, E, EM, M, MH, H):
            if E < guess:
                if E + EM < guess:
                    return False
                else:
                    EM -= guess - E
            if H < guess:
                if MH + H < guess:
                    return False
                else:
                    MH -= guess - H
            if M < guess:
                if EM + M + MH < guess:
                    return False
            return True
            
        start, end = min(E, EM, M, MH, H), max(E + EM, EM + M + MH, MH + H)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if valid(mid, E, EM, M, MH, H):
                start = mid
            else:
                end = mid
        return end if valid(end, E, EM, M, MH, H) else start
