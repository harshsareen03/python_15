# def func1():
#     print('this is harsh sareen')

# func2=func1
# del func1
# func2()

# def func1(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=func1(1)
# print(a)

# def executor(func):
#     func('hello')

# executor(print)


def func1(func):
    def hello():
        print('hello')
        func()
        print('hi this is func')
    return hello

@func1
def kl():
    print('this is kl')

kl()
