class FibonacciComparison:
    def bottom_up(self, n:int) -> int:
        """ 
        Using Tabulation (iterative)
        TIme:O(n), Space: O(n)
        """
        if n <= 1:
            return n
        
        # Initializing table
        dp = [0] * (n * 1)
        dp[1] = 1
        
        # Build to solution
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]