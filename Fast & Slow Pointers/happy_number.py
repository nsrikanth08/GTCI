def happy_number(num):
    slow, fast =  num, num
    while True:
        slow = find_squares_sum(slow)
        fast = find_squares_sum(find_squares_sum(fast))
        if fast == slow:
            break
    return slow == 1

def find_squares_sum(num):
    total = 0
    while(num > 0):
        digit = num % 10
        total += digit * digit
        num //= 10
    return total

def main():
    print(str(happy_number(23)))
    print(str(happy_number(12)))

if __name__ == "__main__":
    main()