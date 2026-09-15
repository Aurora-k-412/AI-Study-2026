from collections import Counter
from collections import defaultdict

#Week_2 小代码练习 Counter
nums = [3, 5, 3, 8, 5, 3]

print(Counter(nums))


#分组 defaultdict()    "".join(sorted(word))
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

#遍历
for word in words:
    key = "".join(sorted(word))
    groups[key].append(word)

print(groups)


#Two Sum + dict
two_sum_nums = [3, 8, 5, 12]
two_sum_target = 13

seen = {}

for index,num in enumerate(two_sum_nums):
    need = two_sum_target - num

    if need in seen:
        print([seen[need],index])
    else:
        seen[num] = index

print()

#前缀和复习
prefix_nums = [3, 5, 2, 6]

prefix_list = [0]
prefix = 0

for num in prefix_nums:
    prefix = prefix + num
    prefix_list.append(prefix)

print(prefix_list)


#栈和有效括号
bracket_text = "{[()]}"

review_vaild = True

review_stack = []
review_pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for char in bracket_text:
    if char in "{[(":
        review_stack.append(char)
    elif char in ")]}":
        if not review_stack:
            review_vaild = False
            print("不匹配")
            break

        elif review_pairs[char] == review_stack[-1]:
            print("匹配")
            review_stack.pop()
        else:
            review_vaild = False
            print("不匹配")
            break

if not review_stack and review_vaild:
    print("合法")

else:
    print("不合法")

print()

#deque队列小练习
from collections import deque

review_queue = deque(["A", "B", "C"])

print(review_queue.popleft())
print(review_queue)
print()


#综合练习1
review_nums = [1, 2, 2, 3, 3, 3, 4]

print([num for num,count in Counter(review_nums).most_common(2)])

print()

#综合练习2
review_two_sum = [6, 3, 8, 2, 7]
review_target = 10

review_seen = {}

for index,num in enumerate(review_two_sum):
    need = review_target - num

    if need in review_seen:
        print([review_seen[need],index])
        break

    else:
        review_seen[num] = index

print()

#sorted+lambda
students_review = [
    {"name": "A", "score": 82},
    {"name": "B", "score": 95},
    {"name": "C", "score": 88}
]

sorted_score = sorted(students_review, key = lambda student: student["score"], reverse = True)

print(sorted_score)

print()

#week2 last 综合小测
review_text = "swiss"

count = Counter(review_text)
print(count)

for index,char in enumerate(review_text):
    if count[char] == 1:
        print(char)
        print(index)
        break

print()

#装饰器小练习

def log_call(func):
    def wrapper(*args,**kwargs):
        print("函数开始执行")

        func(*args,**kwargs)

    return wrapper

@log_call
def add(a,b):
    print(a+b)

add(3,5)
