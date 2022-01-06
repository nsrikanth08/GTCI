import math
def longest_substring_with_k_distinct_chars(k, str):
    longest = -math.inf
    windowStart = 0
    charCount = {}
    for windowEnd in range (0, len(str)):
        if str[windowEnd] in charCount:
            charCount[str[windowEnd]] += 1
        elif len(charCount) >= k:
            if charCount[str[windowStart]] == 1:
               del charCount[str[windowStart]]
            else:
                charCount[str[windowStart]] -= 1
            windowStart += 1
            charCount[str[windowEnd]] = 1
        else:
            charCount[str[windowEnd]] = 1
        longest = max(longest, windowEnd - windowStart + 1)
        
    if longest == -math.inf:
        return 0
    return longest

def main():
    print("Length of longest substring: " + str(longest_substring_with_k_distinct_chars(2, "araaci")))
    print("Length of longest substring: " + str(longest_substring_with_k_distinct_chars(1, "araaci")))
    print("Length of longest substring: " + str(longest_substring_with_k_distinct_chars(3, "cbbebi")))

if __name__ == "__main__":
    main()