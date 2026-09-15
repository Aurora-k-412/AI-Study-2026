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

