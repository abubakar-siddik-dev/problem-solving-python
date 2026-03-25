# Problem: Binary Search (sorted array)

arr = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))

low = 0
high = len(arr) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print(f"Found at index {mid}")
        found = True
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Not found")
