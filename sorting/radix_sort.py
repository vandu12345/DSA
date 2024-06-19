def radix_sort(arr):
    # Find the maximum element to determine the number of digits
    max_value = max(arr)
    max_digits = len(str(abs(max_value)))

    # Perform counting sort for each digit
    for digit in range(max_digits):
        counting_sort(arr, digit)

def counting_sort(arr, digit):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count the occurrences of each digit
    for i in range(n):
        index = (arr[i] // (10 ** digit)) % 10
        count[index] += 1

    # Calculate the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // (10 ** digit)) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
