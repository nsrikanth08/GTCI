def fruits_into_basket(fruits):
    windowStart, result = 0, 0
    baskets = {}
    for windowEnd in range (0, len(fruits)):
        rightFruit = fruits[windowEnd]
        if rightFruit not in baskets:
            baskets[rightFruit] = 0
        baskets[rightFruit] += 1
        while len(baskets) > 2:
            leftFruit = fruits[windowStart]
            baskets[leftFruit] -= 1
            if baskets[leftFruit] == 0:
                del baskets[leftFruit]
            windowStart += 1
        result = max(result, windowEnd - windowStart + 1)
    return result
            
def main():
    print("Maximum number of fruits: " + str(fruits_into_basket(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C'])))

if __name__ == "__main__":
    main()