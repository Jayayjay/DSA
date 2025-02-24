class FibonacciComparison:
    def top_down(self, n:int) -> int:
        """ 
        Top-down approach(memoization) using recursion 
        Time: O(n), Space complexity: O(n)
        """
        def fib_memo(n:int , memo: dict) -> int:
            # Base case
            if n <= 1:
                return n
            
            #check if already calculated
            if n in memo:
                return memo[n]
            
        # calculate and store result
            memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
            return memo[n]
        
        return fib_memo(n, {})
        