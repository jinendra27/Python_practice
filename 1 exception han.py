# if True
#     print("hello")

# print(7/0)

# def Sal(amount):
#     return amount * .10 + amount
#
# print(Sal(50000))

# print('Hello')
# num = int(input('Please enter the value one'))
# num2 = int(input('Please enter the value one'))
# print(num+num2)
# print('This is important line which need to be print on console')


# h = [1,2,3,4]
# for i in range(5):
#     print(h[i])

# f = open('hello.txt','w')
# num = int(input('Please enter the value one'))
# num2 = int(input('Please enter the value one'))
# f.write(str(num + num2))
# f.close()

# print("hello"+3)
#
# try:
#     f = open('hello2.txt','w')
#     num = int(input('Please enter the value one'))
#     num2 = int(input('Please enter the value one'))
#     #f.write(2) #2 '2'
#     f.write(str(num / num2))
# except ZeroDivisionError:
#     print('Please donot use 0 in division ')
#     try:
#         num = int(input('Please enter the value one'))
#         num2 = int(input('Please enter the value one'))
#         f.write(str(num / num2))
#     except ZeroDivisionError:
#         print('Please learn Mathematics, chances are over')
#     except ValueError:
#         print("value error")
#     else:
#         print("else2")
#
#
#
# except TypeError:
#     print('Please Enter the correct input')
#
# except ValueError:
#     print("value error")
# else:
#     print('Hello')
#
#
# finally:
#     print('Finally always executes')
#     f.close()



class MyException(Exception):
    def _init_(self,msg):
        self.msg = msg

accouts = {'chinmay':440,'shusmita':50000,'pratik':100000}
def belowFive(dict):
    for key , val in dict.items():
        if val < 500:
            raise MyException('Balance cannot be below 500')
try:
    belowFive(accouts)

except MyException as e:
    print(e)

except Exception as e:
    print(e)

else:
    print('All bal are fine')
finally:
    print("happy ending'")
