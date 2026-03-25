# Problem: Two Sum
# Find two numbers that add up to target

nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

found = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"Pair found: {nums[i]}, {nums[j]}")
            found = True
            break
    if found:
        break

if not found:
    print("No pair found")
