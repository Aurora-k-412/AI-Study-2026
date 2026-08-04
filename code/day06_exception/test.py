#Day06_tarin01

while True:
    try:
        num = int(input("请输入数字: "))
        print(num)
        break
    except ValueError:
        print("请输入数字")
    except ZeroDivisionError:
        print("不能输入0")
