# Greedy Job Sequencing with Deadlines

jobs = [
    ("J1", 2, 100),
    ("J2", 1, 50),
    ("J3", 2, 80),
    ("J4", 1, 40),
    ("J5", 3, 60)
]

# Sort jobs by decreasing profit
jobs.sort(key=lambda x: x[2], reverse=True)

# Find maximum deadline
max_deadline = 0

for job in jobs:
    if job[1] > max_deadline:
        max_deadline = job[1]

# Create empty time slots
slots = [None] * (max_deadline + 1)

total_profit = 0

# Schedule jobs
for job in jobs:
    job_name = job[0]
    deadline = job[1]
    profit = job[2]

    # Check slots from deadline backwards
    for slot in range(deadline, 0, -1):
        if slots[slot] is None:
            slots[slot] = job_name
            total_profit = total_profit + profit
            break

# Display result
print("Job Schedule:")

for slot in range(1, max_deadline + 1):
    if slots[slot] is not None:
        print("Slot", slot, ":", slots[slot])

print("Maximum Profit:", total_profit)
