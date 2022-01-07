def remove_duplicates(arr):
    duplicateCount = 0
    firstPointer, lastPointer = 0, 0
    while lastPointer < len(arr):
        if firstPointer == lastPointer:
            lastPointer += 1
        else:
            if arr[firstPointer] == arr[lastPointer]:
                duplicateCount += 1
                lastPointer += 1
            else:
                firstPointer = lastPointer
    return len(arr) - duplicateCount

def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))

if __name__ == "__main__":
    main()