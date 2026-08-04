from students import load_students


students = load_students()

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
                s["name"]
                s["age"]
                s["score"]
            )
    elif choice == "2":

        pass

    elif choice == "3":

        total_score = 0

        for s in students:

            total_score += s["score"]

        print("平均成绩为: ", total_score / len(students))

    elif choice == "4":

        break
