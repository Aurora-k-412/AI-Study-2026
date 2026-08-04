students = []

def load_students():

    try:
        with open("students.txt", "r") as f:

            lines = f.readlines()

            for line in lines:
                data = line.strip().split(",")

                student = {
                    "name": data[0],
                    "age": int(data[1]),
                    "score": int(data[2])
                }

                students.append(student)
    except FileNotFoundError:
        print("学生文件不存在")

    return students


# Day06 练习3 学生信息输入校验


def input_student():

    student = []

    while True:

        try:
            name = input("请输入姓名: ")

            age = int(input("请输入年龄: "))

            score = int(input("请输入成绩: "))


            if score < 0 or score > 100:
                raise ValueError("成绩范围错误")


            student = {
                "name": name,
                "age": age,
                "score": score
            }


            return student


        except ValueError as e:

            print("输入错误:", e)
            print("请重新输入\n")



def add_student(student):

    pass



def show_students(students):

    print("\n学生列表:")

    for student in students:

        print(
            f"姓名:{student['name']} "
            f"年龄:{student['age']} "
            f"成绩:{student['score']}"
        )


def average_score():

    pass
