class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.mini = float('inf')
        if amount == 0: return 0
        def findCoin(coins,curr_sum, num_coins,amount):
            if num_coins >= self.mini:
                return -1
            for coin in coins:
                if curr_sum + coin == amount:
                    if self.mini > num_coins+1:
                        self.mini = num_coins+1
                elif curr_sum + coin < amount:
                    findCoin(coins, curr_sum + coin, num_coins+1 ,amount)
                else:
                    return -1

        findCoin(coins, 0, 0, amount)
        return self.mini if self.mini!= float('inf') else -1 
