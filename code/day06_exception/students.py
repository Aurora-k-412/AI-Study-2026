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
