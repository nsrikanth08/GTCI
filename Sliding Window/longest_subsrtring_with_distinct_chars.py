def longest_substring_with_distint_chars(str):
    windowStart, result = 0, 0
    chars = {}
    for windowEnd in range (0, len(str)):
        print(chars)
        rightChar = str[windowEnd]
        if rightChar in chars:
            windowStart = max(windowStart, chars[rightChar] + 1)
        chars[rightChar] = windowEnd
        result = max(result, windowEnd - windowStart + 1)
    return result




def main():
    print("Length of longest substring: " + str(longest_substring_with_distint_chars("aabccbb")))
    print("Length of longest substring: " + str(longest_substring_with_distint_chars("abbbb")))
    print("Length of longest substring: " + str(longest_substring_with_distint_chars("abccde")))

if __name__ == "__main__":
    main()