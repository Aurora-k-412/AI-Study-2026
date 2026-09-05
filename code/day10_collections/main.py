from collections import Counter
from collections import defaultdict
from collections import deque

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



students = [
    ("Alice", "AI"),
    ("Bob", "CS"),
    ("Charlie", "AI"),
    ("David", "CS"),
    ("Eva", "AI")
]

student_major_count = defaultdict(list)
for student, major in students:
    student_major_count[major].append(student)

print(student_major_count)



from collections import deque

queue = deque([10, 20, 30])

queue.append(40)       #右边加40
queue.appendleft(0)    #左边加0
print(queue)

queue.pop()         #删右边
queue.popleft()     #删左边
print(queue)

