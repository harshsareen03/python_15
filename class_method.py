# class kl:
#     def __init__(self,x,t,y):
#         self.x=x
#         self.t=t
#         self.y=y

#     @classmethod
#     def gh(cls,string):
#         return cls(*string.split('*'))

# ght=kl.gh('2*5*6')
# print(ght.t) 




class employee:
    no_of_set=10

    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position =position 

    def printn(self):
        return f'this is {self.name},my salary is {self.salary},my postion is {self.position}'

    # @classmethod
    # def yu(cls,noset):
    #     cls.no_of_set=noset

    @classmethod
    def iot(cls,string):
        return cls(*string.split('-'))

    @staticmethod
    def printhj(string):
        print('this is hj'+string)

io=employee('harsh',1010000,'full stack developer')
op=employee.iot('harsh-800-python devloper')
# print(io.no_of_set)
# print(employee.no_of_set(50))

# print(io.printn())

print(op.position)

employee.printhj('harsh')