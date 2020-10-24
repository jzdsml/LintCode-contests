class Solution:
    """
    @param b: 
    @param c: 
    @param p: 
    @return: return the a
    """
    def lotteryDraw(self, b, c, p):
        # Guess with binary search to find answer.
        # Expectation of X = sum of probability(x) * x, where x are all possible values of X.
        # Probability of the good item comes out in the i-th step = (probability of it never comes out in previous i - 1 steps) * (probability of it comes out in the current step)
        # Probability of the good item never comes out in previous i - 1 steps = (1 - p_1) * (1 - p_2) * ... * (1 - p_{i-1}), where p_j is the probability of it comes out in j-th step.
        
        def get_p(a):
            probs = [a]
            while probs[-1] < 100 and len(probs) <= b - 2:
                probs.append(a)
            while probs[-1] < 100:
                probs.append(min(probs[-1] + c, 100))
            N = len(probs)
            exp = 0
            not_chosen_preprod = 1
            for i in range(N):
                preprod = not_chosen_preprod * probs[i] / 100
                not_chosen_preprod *= (1 - probs[i] / 100)
                exp += preprod * (i + 1)
            p_guess = 100 / exp
            return p_guess
            
        left = 1
        ACCURACY = 0.0001
        right = 100 / ACCURACY
        e = 1 / 10000
        while left + 1 < right:
            guess = left + (right - left) // 2
            if abs(get_p(guess * ACCURACY) - p) < e:
                return guess * ACCURACY
            elif get_p(guess * ACCURACY) > p:
                right = guess
            elif get_p(guess * ACCURACY) < p:
                left = guess
                
        if  abs(get_p(left) - p) >= abs(get_p(right) - p):
            return right * ACCURACY
        else:
            return left * ACCURACY
