def pair_with_target_sum(arr, target):
    firstPointer = 0
    lastPointer = len(arr) - 1
    while firstPointer < lastPointer:
        currSum = arr[firstPointer] + arr[lastPointer]
        print(currSum)
        if currSum == target:
            return [firstPointer, lastPointer]
        elif currSum < target:
            firstPointer += 1
        else:
            lastPointer -= 1
    return [-1, -1]

def main():
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))

if __name__ == "__main__":
    main()