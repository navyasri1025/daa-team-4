# Divide-and-Conquer Matrix Multiplication using Strassen's Algorithm

## Description

This project implements Strassen's matrix multiplication algorithm using the Divide-and-Conquer technique in C++. Matrix multiplication is a fundamental operation in computer science and is widely used in scientific computing, computer graphics, simulations, and numerical applications.

In the conventional matrix multiplication method, each element of the resultant matrix is calculated by multiplying the corresponding row of the first matrix with the corresponding column of the second matrix. The basic divide-and-conquer method divides the matrices into four submatrices and requires eight recursive multiplications.

Strassen's algorithm improves this approach by reducing the number of recursive multiplications from eight to seven. It divides each input matrix into four quadrants, calculates seven intermediate products using matrix addition and subtraction, and combines these products to construct the four quadrants of the final resultant matrix.

The program uses recursive function calls to continue dividing the matrices until the base case is reached. At the base case, individual elements are multiplied directly. The implementation also includes helper functions for matrix addition, subtraction, extracting submatrices, and combining the result quadrants.

A visualization is created using prompt engineering to represent the complete algorithmic process, including matrix division, recursive products, and the combination of the final result.

## Algorithm

1. Start the program.
2. Read the order n of the two square matrices.
3. Validate that n is a positive power of two.
4. Read the elements of matrices A and B.
5. If n = 1, multiply the individual elements and return the result.
6. Otherwise, divide each matrix into four submatrices.
7. Calculate the seven intermediate products M1, M2, M3, M4, M5, M6, and M7 recursively.
8. Use the intermediate products to calculate C11, C12, C21, and C22.
9. Combine the four result quadrants into matrix C.
10. Display the resultant matrix.
11. Stop the program.

### Strassen's Formulas

M1 = (A11 + A22)(B11 + B22)

M2 = (A21 + A22)B11

M3 = A11(B12 - B22)

M4 = A22(B21 - B11)

M5 = (A11 + A12)B22

M6 = (A21 - A11)(B11 + B12)

M7 = (A12 - A22)(B21 + B22)

The result quadrants are calculated as follows:

* C11 = M1 + M4 - M5 + M7
* C12 = M3 + M5
* C21 = M2 + M4
* C22 = M1 - M2 + M3 + M6

The four quadrants are then combined to obtain the final matrix C.

## Prompt Used

"Create a detailed educational flowchart for Strassen's matrix multiplication algorithm using the Divide-and-Conquer approach. Show the input matrices A and B, the base case, division into four quadrants, all seven recursive products M1 to M7 with their formulas, the calculation of the four resultant quadrants C11, C12, C21 and C22, and the assembly of the final product matrix C. Include the recurrence relation T(n) = 7T(n/2) + O(n²) and time complexity O(n^log2(7)) ≈ O(n^2.807). Use clear arrows, readable formulas, and a clean academic design suitable for a college DAA project."

## Output

The program accepts two square matrices and displays their product using Strassen's algorithm. The implementation supports matrix orders that are positive powers of two, such as 1, 2, 4, and 8.

### Sample Input

Matrix order:

```text
2
```

Matrix A:

```text
1 2
3 4
```

Matrix B:

```text
5 6
7 8
```

### Expected Output

```text
Strassen's Matrix Multiplication
Enter the order of square matrices: 2
Enter elements of Matrix A:
Enter elements of Matrix B:

Resultant Matrix (A x B):
19 22
43 50

Time Complexity: O(n^log2(7)) approximately O(n^2.807)
```

### Visualization

The file `Visualization.png` contains a flowchart illustrating the Divide-and-Conquer process, the seven Strassen products, and the construction of the resultant matrix.

## Learning Outcome

* Understood the Divide-and-Conquer technique and its three main stages: Divide, Conquer, and Combine.
* Learned how recursive function calls can be used to solve matrix multiplication problems.
* Understood the division of square matrices into four smaller submatrices.
* Learned the seven intermediate multiplication formulas used in Strassen's algorithm.
* Understood how matrix addition and subtraction are used to combine intermediate products.
* Compared Strassen's seven recursive multiplications with the eight multiplications in the basic divide-and-conquer method.
* Learned the recurrence relation and time complexity of Strassen's algorithm.
* Practiced writing C++ programs using vectors, helper functions, and recursion.
* Developed skills in prompt engineering for generating algorithm visualizations.
* Practiced project documentation and organizing files in a shared GitHub repository.

## Conclusion

Strassen's matrix multiplication algorithm demonstrates how a computational problem can be divided into smaller subproblems and solved recursively. By reducing the number of recursive matrix multiplications from eight to seven, it achieves a better asymptotic time complexity than conventional cubic-time matrix multiplication. This project provides practical experience with recursion, matrix operations, algorithm analysis, and visualization-based learning.
