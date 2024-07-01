from itertools import combinations

def fractional_knapsack_brute_force(items, capacity):
    max_value = 0
    best_combination = []

    n = len(items)

    for r in range(n + 1):
        for combo in combinations(items, r):
            total_weight = sum(item[1] for item in combo)
            total_value = sum(item[0] for item in combo)

            if total_weight <= capacity:
                remaining_capacity = capacity - total_weight
                current_value = total_value
                combination = list(combo)

                for item in items:
                    if item not in combo:
                        if remaining_capacity > 0:
                            weight_to_take = min(remaining_capacity, item[1])
                            value_fraction = (weight_to_take / item[1]) * item[0]
                            current_value += value_fraction
                            combination.append((value_fraction, weight_to_take))
                            break

                if current_value > max_value:
                    max_value = current_value
                    best_combination = combination

    return max_value, best_combination

def knapsack_0_1_brute_force(items, capacity):
    n = len(items)
    max_value = 0
    best_combination = []

    for r in range(1, n+1):
        for combo in combinations(items, r):
            total_weight = sum(item[1] for item in combo)
            total_value = sum(item[0] for item in combo)
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_combination = combo

    return max_value, best_combination

def fractional_knapsack_greedy(items, capacity):
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    max_value = 0
    best_combination = []

    for value, weight in items:
        if capacity > 0 and weight <= capacity:
            capacity -= weight
            max_value += value
            best_combination.append((value, weight))
        else:
            fraction = capacity / weight
            max_value += value * fraction
            best_combination.append((value * fraction, weight * fraction))
            break

    return max_value, best_combination

def knapsack_0_1_dp(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            value, weight = items[i-1]
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]

    max_value = dp[n][capacity]

    w = capacity
    best_combination = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            value, weight = items[i-1]
            best_combination.append((value, weight))
            w -= weight

    return max_value, best_combination

def main():
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 40

    fractional_value, fractional_combination = fractional_knapsack_brute_force(items, capacity)
    print("Fractional Knapsack (Brute-force):")
    print(f"Maximum value: {fractional_value}")
    print(f"Best combination: {fractional_combination}\n")

    knapsack_value, knapsack_combination = knapsack_0_1_brute_force(items, capacity)
    print("0/1 Knapsack (Brute-force):")
    print(f"Maximum value: {knapsack_value}")
    print(f"Best combination: {knapsack_combination}\n")
    
    fractional_value, fractional_combination = fractional_knapsack_greedy(items, capacity)
    print("Fractional Knapsack (Greedy):")
    print(f"Maximum value: {fractional_value}")
    print(f"Best combination: {fractional_combination}\n")

    knapsack_value, knapsack_combination = knapsack_0_1_dp(items, capacity)
    print("0/1 Knapsack (Dynamic Programming):")
    print(f"Maximum value: {knapsack_value}")
    print(f"Best combination: {knapsack_combination}")

if __name__ == "__main__":
    main()
