def selectionSort(array, size):
    for index in range(size):
        min_index = index

        for j in range(index + 1, size):

            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j

        # swapping the elements to sort the array
        (array[index], array[min_index]) = (array[min_index], array[index])

def main1():
    arr_size = int(input("Enter size of array: "))
    arr = []

    for i in range(arr_size):
        value = int(input("Enter value: "))
        arr.append(value)

    print("\nUnsorted array is: {}".format(arr))
    size = len(arr)
    selectionSort(arr, size)
    print("\nSorted array is: {}".format(arr))

#main1()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def job_scheduling(jobs):
    # Sort the jobs based on their finish times in non-decreasing order
    jobs.sort(key=lambda x: x[1])

    schedule = []  # Initialize the schedule

    # Keep track of the maximum finish time
    max_finish_time = 0

    for job in jobs:
        start_time = job[0]
        finish_time = job[1]

        # Check if the job can be scheduled without overlapping
        if start_time >= max_finish_time:
            schedule.append(job)
            max_finish_time = finish_time

    return schedule


# Example usage
jobs = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
schedule = job_scheduling(jobs)

# Print the scheduled jobs
for job in schedule:
    print(f"Job start time: {job[0]}, Job finish time: {job[1]}")
