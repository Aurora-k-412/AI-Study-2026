class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
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
