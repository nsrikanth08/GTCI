def squaring_a_sorted_array(arr):
    leftPtr, rightPtr = 0, len(arr) - 1
    topIndex = len(arr) - 1
    result = [0 for x in range(0, len(arr))]
    while leftPtr <= rightPtr:
        leftSquare = arr[leftPtr] * arr[leftPtr]
        rightSquare = arr[rightPtr] * arr[rightPtr]
        if leftSquare > rightSquare:
            result[topIndex] = leftSquare
            leftPtr += 1
        else:
            result[topIndex] = rightSquare
            rightPtr -= 1
        topIndex -= 1
    return result

def main():
    print("Squares: " + str(squaring_a_sorted_array([-2, -1, 0, 2, 3])))
    print("Squares: " + str(squaring_a_sorted_array([-3, -1, 0, 1, 2])))

if __name__ == "__main__":
    main()