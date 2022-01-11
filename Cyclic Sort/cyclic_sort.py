def cyclic_sort(nums):
    for i in range(0, len(nums)):
        while nums[i] != i+1:
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
    return nums

def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))

if __name__ == "__main__":
    main()