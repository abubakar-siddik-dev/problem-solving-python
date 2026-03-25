# Problem: Remove duplicate characters

s = input("Enter string: ")

result = ""
for char in s:
    if char not in result:
        result += char

print("Result:", result)
