import random
import time
import matplotlib.pyplot as plt


# -----------------------------
# Merge Sort
# -----------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -----------------------------
# Quick Sort
# -----------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


# -----------------------------
# Measure Execution Time
# -----------------------------
def measure_time(sort_function, data):

    start = time.perf_counter()

    sort_function(data.copy())

    end = time.perf_counter()

    return end - start


# -----------------------------
# Main Program
# -----------------------------
def main():

    input_sizes = [10, 100, 1000]

    merge_times = []
    quick_times = []

    print("Sorting Complexity Comparison")
    print("--------------------------------")

    for n in input_sizes:

        data = [random.randint(1, 10000) for _ in range(n)]

        merge_time = measure_time(merge_sort, data)
        quick_time = measure_time(quick_sort, data)

        merge_times.append(merge_time)
        quick_times.append(quick_time)

        print(f"n = {n}")
        print(f"Merge Sort Time : {merge_time:.8f} seconds")
        print(f"Quick Sort Time : {quick_time:.8f} seconds")
        print()

    # -----------------------------
    # Create Visualization
    # -----------------------------
    plt.figure(figsize=(9, 6))

    plt.plot(
        input_sizes,
        merge_times,
        marker="o",
        label="Merge Sort"
    )

    plt.plot(
        input_sizes,
        quick_times,
        marker="o",
        label="Quick Sort"
    )

    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")

    plt.title("Sorting Complexity: Merge Sort vs Quick Sort")

    plt.xticks(input_sizes)

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    # Save graph
    plt.savefig("Visualization.png", dpi=300)

    plt.show()

    print("Visualization saved as Visualization.png")


# Run program
if __name__ == "__main__":
    main()