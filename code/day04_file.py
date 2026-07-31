print("Day04 Python File")


with open("learning.txt","w") as f:
    f.write("Python File Learning\n")
    f.write("AI Study 2026\n")


with open("learning.txt","r") as f:
    content = f.read()


print(content)



# Day04 小练习1：保存学生信息

students = [
    "凯凯,20,95\n",
    "小明,21,88\n",
    "小红,19,92\n"
]
#写入文件
with open("students.txt","w") as f:
    for student in students:
        f.write(student)

#读取文件
with open("students.txt","r") as f:
    content = f.read()

print("学生信息：\n" + content)



