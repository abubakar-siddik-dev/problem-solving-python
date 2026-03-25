s = input("Enter string: ").lower()
vowels = "aeiou"

count = 0
for ch in s:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
