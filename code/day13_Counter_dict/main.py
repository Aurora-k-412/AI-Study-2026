from collections import Counter
from collections import defaultdict

s_1 = "listen"
t = "silent"

if Counter(s_1) == Counter(t):
    print("是异位词")
else:
    print("不是异位词")

s = "swiss"

#第一次遍历,统计每个字符出现的次数
count_s = Counter(s)

#第二次遍历原字符串
for char in s:
    if count_s[char] == 1:
        print(char)
        break


#两个数组求交集 —— set实战
nums1 = [2, 5, 7, 9]
nums2 = [1, 5, 8, 9]

#将nums2转为set
nums2_set = set(nums2)
result_1 = []

for num in nums1:
    if num in nums2_set:
        result_1.append(num)

print(result_1)


#异位词分组—— defaultdict(list)实战
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

#遍历
for word in words:
    key = "".join(sorted(word))
    groups[key].append(word)
print(groups)

#"".join(sorted(word))这个重点记一下

nums = [4, 4, 1, 1, 1, 2, 2, 3]
k = 2

freq = Counter(nums)

most_sum = freq.most_common(k)

result_2 = [num for num,freq in most_sum]
print(result_2)
