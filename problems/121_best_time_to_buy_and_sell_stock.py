class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        answer = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > answer:
                answer = prices[i] - min_price
        return answer
