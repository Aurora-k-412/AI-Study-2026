import students


student_list = students.input_student()


students.show_students(student_list)


print("\n学生信息")
print(student_list)


while True:

    print("""
        ======学生管理系统======

        1.查看学生
        2.添加学生
        3.平均成绩
        4.退出
    """)

    choice = input("请输入选项: ")

    if choice == "1":

        for s in students:

            print(
                s["name"],
                s["age"],
                s["score"]
            )
    elif choice == "2":

        name = input("请输入学生姓名: ")

        try:
            age = int(input("请输入学生年龄: "))

        except ValueError:
            print("年龄必须是数字")
            continue


        try:
            score = int(input("请输入学生成绩: "))

            if score < 0 or score > 100:

                print("成绩范围错误")
                continue

        except ValueError:
            print("成绩必须是数字")
            continue


        student = {
            "name": name,
            "age": age,
            "score": score
        }

        students.append(student)

        print("添加学生成功")

    elif choice == "3":

        total_score = 0

        for s in students:

            total_score += s["score"]

        print("平均成绩为: ", total_score / len(students))

    elif choice == "4":

        break
