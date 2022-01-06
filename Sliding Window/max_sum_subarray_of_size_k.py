def max_subarray_of_size_k(k, arr):
    windowStart, currSum, maxSum = 0, 0, 0
    for windowEnd in len(arr):
        currSum += arr[windowEnd]
        if windowEnd >= k-1:
            maxSum = max(currSum, maxSum)
            currSum -= arr[windowStart]
            windowStart += 1
    return maxSum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_subarray_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_subarray_of_size_k(2, [2, 3, 4, 1, 5])))
