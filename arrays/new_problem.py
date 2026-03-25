# Problem: Find minimum number in array

nums = list(map(int, input("Enter numbers: ").split()))

minimum = nums[0]

for num in nums:
    if num < minimum:
        minimum = num

print("Minimum:", minimum)
