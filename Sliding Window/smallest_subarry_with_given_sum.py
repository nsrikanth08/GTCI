import math
def smallest_subarray_with_given_sum(s, arr):
    smallest = math.inf
    windowStart, summ = 0, 0

    for windowEnd in range (0, len(arr)):
        summ += arr[windowEnd]

        while summ >= s:
            smallest = min(smallest, windowEnd - windowStart + 1)
            summ -= arr[windowStart]
            windowStart += 1
    if smallest == math.inf:
        return 0
    return smallest

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))

if __name__ == '__main__':
    main()