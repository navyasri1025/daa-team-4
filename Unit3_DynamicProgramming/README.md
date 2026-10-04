# 0/1 Knapsack Problem using Dynamic Programming

## Description

This project implements the 0/1 Knapsack problem using Dynamic Programming and visualizes the DP table for 4 items with a maximum capacity of 10.

The visualization shows the maximum value that can be obtained for each combination of items and capacity.

## Algorithm

### Pseudocode

```text
Start

Input item weights, values, and knapsack capacity

Initialize DP table with 0

For each item i:
    For each capacity w:
        If weight of item i <= w:
            DP[i][w] = max(
                DP[i-1][w],
                value[i] + DP[i-1][w-weight[i]]
            )
        Else:
            DP[i][w] = DP[i-1][w]

Display the DP table

The last cell gives the maximum possible value

End
```

## Prompt Used

“Draw a DP table for 0/1 Knapsack with 4 items and capacity 10. Show the item inclusion and exclusion decisions and highlight the maximum value.”

## Output

The generated visualization shows the complete 0/1 Knapsack DP table with 4 items and capacity 10.

**Maximum value obtained: 12**

The output visualization is saved as:

`Visualization.png`

## Learning Outcome

* Understood the 0/1 Knapsack problem.
* Learned how Dynamic Programming avoids repeated calculations.
* Understood item inclusion and exclusion decisions.
* Learned how to construct and interpret a DP table.
* Practiced prompt-based visualization.
* Practiced GitHub project documentation.
