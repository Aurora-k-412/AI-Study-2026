from student import Student, GraduateStudent ,Teacher


s1 = Student("Bob", 20, 75)
s2 = GraduateStudent("Alice", 24, 95, "AI Research")
s3 = GraduateStudent("Charlie", 26, 91, "Computer Vision")
teacher = Teacher("Tom", "Python")

people = [s1, s2, s3, teacher]

def check_person(person):
    match person:
        case GraduateStudent():
            print("这是研究生")
        case Student():
            print("这是普通学生")
        case Teacher():
            print("这是教师")
        case _:
            print("未知类型的人物")

def introduce(person):
    match person:
        case GraduateStudent(name=name, age=age, score=score, thesis_title=thesis_title):
            print(f"研究生 {name}，年龄 {age}，成绩 {score}，论文题目：{thesis_title}")
        case Student(name=name, age=age, score=score):
            print(f"学生 {name}，年龄 {age}，成绩 {score}")
        case Teacher(name=name, course=course):
            print(f"教师 {name}，课程 {course}")
        case _:
            print("未知类型的人物")


    if isinstance(person, GraduateStudent):
        return "研究生"
    elif isinstance(person, Student):
        return "学生"
    elif isinstance(person, Teacher):
        return "教师"
    else:
        return "未知"

def check_person(person):
    if isinstance(person, GraduateStudent):
        print("这是研究生")
    elif isinstance(person, Student):
       print("这是普通学生")
    elif isinstance(person, Teacher):
        print("这是教师")
    else:
        print("未知类型的人物")

def get_role(person):
    if isinstance(person, GraduateStudent):
        return "研究生"
    elif isinstance(person, Student):
        return "学生"
    elif isinstance(person, Teacher):
        return "教师"
    else:
        return "未知"

def show_person_info(person):
    for person in people:
        person.show_info()
        print()  # 打印空行分隔不同人的信息

def cout_roles(people):
    student_count = 0
    graduate_count = 0
    teacher_count = 0
    for person in people:
        if isinstance(person, GraduateStudent):
            graduate_count += 1
        elif isinstance(person, Student):
            student_count += 1
        elif isinstance(person, Teacher):
            teacher_count += 1

    print(f"普通学生: {student_count}")
    print(f"研究生: {graduate_count}")
    print(f"教师: {teacher_count}")

print(show_person_info(people))
cout_roles(people)

check_person(s1)
check_person(s2)
check_person(s3)
check_person(teacher)

print(type(s1))
print(type(s2))
print(type(s3))
print(type(teacher))

print(isinstance(s2, Student))
print(isinstance(s2, GraduateStudent))

print(get_role(s1))
print(get_role(s2))
print(get_role(s3))
print(get_role(teacher))
