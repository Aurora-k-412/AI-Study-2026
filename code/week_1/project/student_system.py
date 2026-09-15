students = []


def add_student():
    name = input("请输入学生姓名：")
    score = input("请输入成绩：")

    student = {
        "name": name,
        "score": score
    }

    students.append(student)
    print("添加成功")


def show_students():
    if len(students) == 0:
        print("暂无学生")
        return

    for student in students:
        print(student)


while True:

    print("\n学生管理系统")
    print("1. 添加学生")
    print("2. 查看学生")
    print("3. 退出")

    choice = input("请选择：")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        break

    else:
        print("输入错误")