import file_utils


students = [

    {
        "name":"小明",
        "age":20,
        "score":90
    },

    {
        "name":"小红",
        "age":19,
        "score":95
    }

]


file_utils.save_students(students)


result = file_utils.load_students()


print(result)
