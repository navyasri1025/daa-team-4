Project 10 – N-Queens Using Backtracking
Unit

Unit IV – Backtracking

Project Title

N-Queens State Space Tree

Description

This project implements the N-Queens problem using the Backtracking algorithm. The program provides an interactive visualization of queen placements, invalid branches, pruning, and backtracking.

The main demonstration is performed for N = 4.

Algorithm

Start with the first row.

Try placing a queen in each column.

Check whether the position is safe.

If safe, place the queen and move to the next row.

If the placement is invalid, reject the branch.

If no valid position is available, backtrack and try another position.

Continue until all queens are placed.

Pseudocode
NQueens(row):

    if row == N:
        record solution
        return

    for each column:
        if position is safe:
            place queen
            NQueens(row + 1)
            remove queen

Prompt Used

The AI prompt used to generate the state-space tree is available in Prompt.txt.

Visualization

The AI-generated state-space tree is available as:

Visualization.png

The visualization shows valid placements, invalid branches, pruning, and backtracking.

Output

The Python program provides an interactive GUI using Tkinter and Matplotlib.

For N = 4, the program finds 2 solutions:

[2, 4, 1, 3]
[3, 1, 4, 2]


All program execution screenshots are combined into:

Output.pdf

Test Cases
Test Case	Input	Expected Output
TC1	N = 4	2 solutions
TC2	N = 8	92 solutions

Both test cases passed successfully.

Complexity

Time Complexity: O(N!)

Space Complexity: O(N)

Learning Outcome

Understood the Backtracking technique.

Learned recursive problem solving.

Understood state-space tree exploration.

Learned pruning of invalid branches.

Created an interactive algorithm visualization.

Technologies Used

Python

Tkinter

Matplotlib

NumPy

Files
Unit4_BackTracking/
│
├── queens.py
├── Prompt.txt
├── Output.pdf
└── README.md