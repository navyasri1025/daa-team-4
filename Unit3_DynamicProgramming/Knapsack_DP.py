import matplotlib.pyplot as plt

# Item weights and values
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]

n = len(weights)
capacity = 10

# Create DP table
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                values[i - 1] + dp[i - 1][w - weights[i - 1]]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Print DP table
print("0/1 Knapsack DP Table")
print("Capacity:", list(range(capacity + 1)))

for i in range(n + 1):
    print("Item", i, ":", dp[i])

# Visualize DP table
fig, ax = plt.subplots(figsize=(12, 5))
ax.axis("off")

table_data = [["Items / Capacity"] + list(range(capacity + 1))]

for i in range(n + 1):
    table_data.append([f"Item {i}"] + dp[i])

table = ax.table(
    cellText=table_data,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)

plt.title("0/1 Knapsack DP Table")
plt.savefig("Visualization.png", bbox_inches="tight")
plt.show()