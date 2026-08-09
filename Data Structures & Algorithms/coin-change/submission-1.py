class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.min_coins = float('inf')
        
        if amount == 0: 
            return 0
        
        def findCoinCombination(coins: List[int], current_sum: int, num_coins: int, target: int) -> None:
            # Early exit if the current number of coins is already greater than or equal to the known minimum
            if num_coins >= self.min_coins:
                return
            
            for coin in coins:
                new_sum = current_sum + coin
                
                if new_sum == target:
                    # Update the minimum number of coins if a new combination uses fewer coins
                    self.min_coins = min(self.min_coins, num_coins + 1)
                elif new_sum < target:
                    # Recurse with the new sum and incremented coin count
                    findCoinCombination(coins, new_sum, num_coins + 1, target)
                else:
                    # No need to continue if the new sum exceeds the target
                    return
        
        findCoinCombination(coins, 0, 0, amount)
        
        # Return the minimum number of coins, or -1 if no valid combination was found
        return self.min_coins if self.min_coins != float('inf') else -1
