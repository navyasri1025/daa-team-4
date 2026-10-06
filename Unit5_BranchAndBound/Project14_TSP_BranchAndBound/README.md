# Project 14: TSP using Branch-and-Bound

## Description

This project implements the **Travelling Salesman Problem (TSP)** using the **Branch-and-Bound** technique.

The objective of TSP is to find the minimum-cost tour that visits every city exactly once and returns to the starting city.

Branch-and-Bound improves the basic exhaustive search by calculating a lower bound for each partial solution. If the estimated cost of a branch is greater than or equal to the best solution already found, that branch is **pruned** and is not explored further.

A search-tree visualization is included to show explored and pruned branches.

## Problem Example

Four cities are considered:

- A
- B
- C
- D

Cost matrix:

|   | A | B | C | D |
|---|---:|---:|---:|---:|
| A | 0 | 10 | 15 | 20 |
| B | 10 | 0 | 35 | 25 |
| C | 15 | 35 | 0 | 30 |
| D | 20 | 25 | 30 | 0 |

The optimal tour is:

**A → B → D → C → A**

Minimum cost:

**80**

## Algorithm / Pseudocode

```text
TSP_Branch_And_Bound(cost_matrix)

1. Calculate an initial lower bound using the two minimum
   outgoing edges of every city.
2. Mark the starting city as visited.
3. Start recursive Branch-and-Bound search.
4. For every unvisited city:
      a. Add the travel cost to the current city.
      b. Calculate the new lower bound.
      c. Calculate:
            estimated_cost = current_cost + new_bound
5. If estimated_cost < best_cost:
      Explore the branch recursively.
6. Otherwise:
      Prune the branch.
7. When all cities are visited:
      Add the cost of returning to the starting city.
8. Update the best tour if its cost is smaller.
9. Return the optimal tour and minimum cost.
```

## Python Program

The file `Project14_TSP_BranchAndBound.py` contains the implementation.

### Expected Output

```text
Optimal Tour: A -> B -> D -> C -> A
Minimum Cost: 80
```

## Visualization

The visualization represents the Branch-and-Bound search tree.

- **Green branches/nodes:** explored promising solutions.
- **Red branches/nodes:** pruned solutions.
- **Dashed red branches:** branches discarded because their estimated cost is not better than the current best solution.
- **Blue node:** starting city.
- **Highlighted final tour:** optimal solution.

## Prompt Used

> Create a clean educational visualization of a Travelling Salesman Problem solved using Branch-and-Bound for 4 cities A, B, C, and D. Show the search tree starting from A. Each node should display the partial tour and its estimated lower-bound cost. Use green for explored/promising branches, red for pruned branches, and clearly mark the optimal tour A → B → D → C → A with minimum cost 80. Include a legend explaining explored, pruned, and optimal paths. Use a white background, readable labels, and a professional computer-science classroom diagram style. The visualization should clearly demonstrate how Branch-and-Bound avoids unnecessary search.

## How Branch-and-Bound is Shown

The search tree contains different possible partial tours. At each level, the algorithm calculates a lower-bound estimate.

If the estimated cost of a branch is worse than the current best complete tour, that branch does not need to be explored. Such branches are shown in **red** in the visualization.

This demonstrates the main advantage of Branch-and-Bound: it reduces the number of solutions that need to be examined compared with brute-force enumeration.

## Learning Outcomes

- Understood the Travelling Salesman Problem.
- Learned the Branch-and-Bound technique.
- Understood lower-bound calculation and pruning.
- Learned how a search tree represents possible solutions.
- Understood how pruning reduces unnecessary computation.
- Practiced documenting an algorithm and creating an AI-assisted visualization.
