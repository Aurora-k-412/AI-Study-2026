def save_students(students):

    with open(
        "students.txt",
        "w",
        encoding="utf-8"
    ) as f:

        for student in students:

            line = (
                f"{student['name']},"
                f"{student['age']},"
                f"{student['score']}\n"
            )

            f.write(line)



def load_students():

    students = []

    try:

        with open(
            "students.txt",
            "r",
            encoding="utf-8"
        ) as f:


            for line in f:

                data = line.strip().split(",")


                student = {
                    "name": data[0],
                    "age": int(data[1]),
                    "score": int(data[2])
                }


                students.append(student)


    except FileNotFoundError:

        print("没有找到学生文件，创建空列表")


    return students



def read_file(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.readlines()

            return content

    except FileNotFoundError as e:

        print("文件不存在",e)
        return None
