from collections import Counter

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]

count = Counter(words)

print(count)
print(count["apple"])

print(count.most_common())
print(count.most_common(2))
