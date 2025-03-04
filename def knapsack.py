def knapsack(capacity, weights, profits, n):
    # ایجاد جدول DP با ابعاد (n+1) * (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # پر کردن جدول DP
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], profits[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][capacity]

# تست الگوریتم با 10 ورودی مختلف
import random
for test in range(10):
    n = random.randint(1, 20)  # تعداد آیتم‌ها
    capacity = random.randint(10, 50)  # ظرفیت کوله‌پشتی
    weights = [random.randint(1, 10) for _ in range(n)]
    profits = [random.randint(10, 100) for _ in range(n)]
    
    max_profit = knapsack(capacity, weights, profits, n)
    print(f"Test {test+1}: n = {n}, Capacity = {capacity}, Max Profit = {max_profit}")
