# Day04 Python 文件操作


with open("test.txt","w") as f:
    f.write("AI Internship\n")
    f.write("Python Learning\n")


with open("test.txt","r") as f:
    content = f.read()


print(content)
