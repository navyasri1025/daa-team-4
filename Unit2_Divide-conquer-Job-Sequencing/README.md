# Greedy Job Sequencing with Deadlines

## DAA Macro Project – Unit II

**Course:** Design and Analysis of Algorithms (DAA)  
**Unit:** Unit II – Divide and Conquer / Greedy  
**Project:** Greedy Job Sequencing Flowchart  
**Team Repository:** daa-team-4

---

## 1. Introduction

Job Sequencing with Deadlines is a classic Greedy Algorithm problem. Each job has a deadline and a profit, and every job requires one unit of time to complete.

The objective is to select and schedule jobs in such a way that the total profit is maximized while completing every selected job before or on its deadline.

The greedy approach selects jobs in decreasing order of their profit and assigns each job to the latest available time slot before its deadline.

---

## 2. Objective

The objectives of this project are:

- To understand the Greedy approach to algorithm design.
- To implement the Job Sequencing with Deadlines algorithm.
- To maximize the total profit by selecting suitable jobs.
- To visualize the decision-making process using a flowchart.
- To demonstrate the working of the algorithm using an example.

---

## 3. Problem Statement

Given a set of jobs where each job has:

- A unique job ID
- A deadline
- A profit

Each job requires exactly one unit of time to complete.

The goal is to schedule the jobs so that:

1. Every selected job is completed before or on its deadline.
2. The total profit is maximized.

---

## 4. Example Input

The following jobs are used for demonstration:

| Job | Deadline | Profit |
|-----|----------|--------|
| J1  | 2        | 100    |
| J2  | 1        | 50     |
| J3  | 2        | 80     |
| J4  | 1        | 40     |
| J5  | 3        | 60     |

---

## 5. Algorithm

### Greedy Job Sequencing with Deadlines

1. Start.
2. Read all jobs along with their deadlines and profits.
3. Sort the jobs in decreasing order of profit.
4. Find the maximum deadline among all jobs.
5. Create empty time slots from 1 to the maximum deadline.
6. Consider each job in decreasing order of profit.
7. Start checking for an available slot from the job's deadline and move backwards.
8. If an empty slot is found, schedule the job in that slot.
9. Add the profit of the scheduled job to the total profit.
10. If no suitable slot is available, skip the job.
11. Repeat the process until all jobs are considered.
12. Display the selected jobs and maximum total profit.
13. Stop.

---

## 6. Pseudocode

```text
Algorithm JobSequencing(jobs)

1. Sort all jobs in decreasing order of profit.

2. Find the maximum deadline.

3. Create empty time slots from 1 to maximum deadline.

4. Set total_profit = 0.

5. For each job in sorted order:
      deadline = job.deadline
      profit = job.profit

      For slot = deadline down to 1:
          If slot is empty:
              Schedule the job in this slot
              total_profit = total_profit + profit
              Break

6. Display the scheduled jobs.

7. Display total_profit.

8. Stop.
