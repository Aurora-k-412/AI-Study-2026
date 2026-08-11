from file_utils import read_file

from students import (
    load_students,
    show_students,
    average_score,
    add_student
)



# 读取文件

lines = read_file("students.txt")


if lines is not None:

    students = load_students(lines)

else:

    students = []



while True:


    print("\n=====学生管理系统=====")

    print("1. 查看学生")

    print("2. 平均成绩")

    print("3. 添加学生")

    print("4. 退出")


    choice = input("请选择:")



    if choice == "1":

        show_students(students)



    elif choice == "2":

        avg = average_score(students)

        print(
            f"平均成绩:{avg}"
        )



    elif choice == "3":

        add_student(students)



    elif choice == "4":

        print("系统退出")

        break



    else:

        print("输入错误，请重新选择")
