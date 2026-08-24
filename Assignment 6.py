# 0/1 Knapsack Problem

def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, remaining_capacity):
        if i == 0 or remaining_capacity == 0:
            return 0

        if (i, remaining_capacity) in memo:
            return memo[(i, remaining_capacity)]

        if weights[i - 1] > remaining_capacity:
            answer = solve(i - 1, remaining_capacity)
        else:
            take = values[i - 1] + solve(
                i - 1,
                remaining_capacity - weights[i - 1]
            )
            skip = solve(i - 1, remaining_capacity)
            answer = max(take, skip)

        memo[(i, remaining_capacity)] = answer
        return answer

    return solve(n, capacity)


def build_knapsack_table(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                skip = dp[i - 1][w]
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                dp[i][w] = max(skip, take)

    return dp


def find_selected_items(dp, weights, capacity):
    n = len(weights)
    w = capacity
    selected = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()
    return selected


def knapsack_bottom_up(weights, values, capacity):
    dp = build_knapsack_table(weights, values, capacity)

    n = len(weights)
    maximum_value = dp[n][capacity]

    selected_items = find_selected_items(
        dp, weights, capacity
    )

    return maximum_value, selected_items


# Main program

weights = [2, 3, 4, 5]
values = [2, 3, 4, 5, 7]
capacity = 5

print("Items:")

for i in range(len(weights)):
    print("Item", i, ": Weight =", weights[i], ", Value =", values[i])

print("Bag Capacity =", capacity)

top_down_answer = knapsack_top_down(
    weights, values, capacity
)

print("\nTop-Down Answer =", top_down_answer)

bottom_up_answer, selected_items = knapsack_bottom_up(
    weights, values, capacity
)

print("Bottom-Up Answer =", bottom_up_answer)
print("Selected Items =", selected_items)

print("\nSelected Items Details:")

total_weight = 0
total_value = 0

for i in selected_items:
    print("Item", i, ": Weight =", weights[i], ", Value =", values[i])

    total_weight += weights[i]
    total_value += values[i]

print("\nTotal Weight =", total_weight)
print("Total Value =", total_value)

if top_down_answer == bottom_up_answer:
    print("\nBoth methods give the same answer.")
else:
    print("\nAnswers are different.")