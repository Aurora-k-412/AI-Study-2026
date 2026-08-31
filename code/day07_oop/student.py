class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print("=== 学生信息 ===")
        print("姓名：",self.name)
        print("年龄：",self.age)
        print("成绩：",self.score)

    def is_passed(self):
        if self.score >= 60:
            return True

        else:
            return False

    def update_score(self,new_score):
        if 0 <= new_score <= 100:
            self.score = new_score
        else:
            raise ValueError("成绩必须在0到100之间")



class GraduateStudent(Student):
    def __init__(self, name, age, score, thesis_title):
        super().__init__(name, age, score)
        self.thesis_title = thesis_title

    # 重写show_info方法
    def show_info(self):
        print("=== 研究生信息 ===")
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("成绩：", self.score)
        print("论文题目：", self.thesis_title)


class Teacher():
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def show_info(self):
        print("=== 教师信息 ===")
        print("姓名：", self.name)
        print("课程：", self.course)

    def is_teaching(self):
        if self.course == "Python":
            return True
        else:
            return False
