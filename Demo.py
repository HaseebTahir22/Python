def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            print("The number is",num)
    return max_num
