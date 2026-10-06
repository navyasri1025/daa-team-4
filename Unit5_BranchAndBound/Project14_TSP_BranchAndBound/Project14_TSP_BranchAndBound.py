# Project 14: TSP using Branch and Bound

INF = 9999

def first_min(adj, i):
    values = [adj[i][j] for j in range(len(adj)) if i != j]
    return min(values)

def second_min(adj, i):
    values = sorted(adj[i][j] for j in range(len(adj)) if i != j)
    return values[1]

def tsp_branch_bound(adj):
    n = len(adj)
    visited = [False] * n
    path = [-1] * (n + 1)
    best_path = []
    best_cost = [INF]

    initial_bound = sum(first_min(adj, i) + second_min(adj, i)
                        for i in range(n)) // 2

    path[0] = 0
    visited[0] = True

    def search(bound, current_cost, level):
        if level == n:
            last = path[level - 1]
            if adj[last][0] != 0:
                total = current_cost + adj[last][0]
                if total < best_cost[0]:
                    best_cost[0] = total
                    best_path.clear()
                    best_path.extend(path[:n])
                    best_path.append(0)
            return

        for city in range(n):
            if not visited[city]:
                last = path[level - 1]
                new_cost = current_cost + adj[last][city]
                new_bound = bound

                if level == 1:
                    new_bound -= (first_min(adj, last) +
                                  first_min(adj, city)) / 2
                else:
                    new_bound -= (second_min(adj, last) +
                                  first_min(adj, city)) / 2

                estimate = new_cost + new_bound

                if estimate < best_cost[0]:
                    path[level] = city
                    visited[city] = True
                    search(new_bound, new_cost, level + 1)
                    visited[city] = False
                # Otherwise this branch is pruned.

    search(initial_bound, 0, 1)
    return best_path, best_cost[0]


# Example: 4-city symmetric cost matrix
cities = ["A", "B", "C", "D"]
adj = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tour, cost = tsp_branch_bound(adj)

print("Optimal Tour:", " -> ".join(cities[i] for i in tour))
print("Minimum Cost:", cost)
