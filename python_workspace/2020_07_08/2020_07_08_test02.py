# def function1(a, b):
#     for i in range(b):
#         print(a)

# function1("dd",10)


# def function2(a, *b):
#     for i in range(a):
#         print(b)

# function2(4,"ss", "qq", ".qqw")

# 매개변수를 미리 정해두면 안써도 돌아간다
def function3(a, n=2):
    for i in range(n):
        print(a)
function3(3)


