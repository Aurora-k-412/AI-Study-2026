from student import Student

s1 = Student("Alice", 20, 85)

s1.show_info()

s2 = Student("Bob", 19, 55)
print(s2.is_passed())  # 输出: False

print(s1.is_passed())
