import sys


def max_profit(prices):
    relevant_mins = relevant_min(prices)
    return cal_max_profit(prices, relevant_mins)


def relevant_min(prices):
    rel_mins = []
    min_val = sys.maxsize
    for price in prices:
        min_val = min(min_val, price)
        rel_mins.append(min_val)
    return rel_mins


def cal_max_profit(prices, relevant_mins):
    max_revenue = 0
    for i, price in enumerate(prices):
        if price > relevant_mins[i]:
            current_revenue = price - relevant_mins[i]
            max_revenue = max(max_revenue, current_revenue)
    return max_revenue


prices = [255, 260, 250, 240, 228, 270, 300, 210, 245]
print(max_profit(prices))
