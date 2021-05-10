# a = lambda x:x*x
# print(a(5))
#
# y = lambda x,y:x if x>y else y
# print(y(4,2))
#
# r = lambda x,y:x+y
# print(r(20,40))
#
# a,b = [int(n) for n in input('enter the no').split(',')]
# print(f'bigger number is {y(a,b)}')
#
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
# listA = [12,14,46,25,464]
# listB = []
# for item in listA:
#     listB.append(is_even(item))
# print(listB)
#
# h = list(filter(is_even,listA))
# print(h)
#
# ha = list(filter(lambda x:(x % 2 == 0),listA))
# print(ha)
#
# h = list(map(lambda x:x+10, listA))
# print(h)

# x = [1,2,3,4,5,6]
#
# a = tuple(map(lambda y:y*y , x))
# print(a)

# import functools
# from functools import reduce
#
# x = [1,2,3,4,5,6]
# a = functools.reduce(lambda y,z:y+z, x)
# print(a)
#
# k = [1,2,3,4,5,6,7]
# j = [1,3,4,5,6,6,7]
#
#
# a = list(map(lambda x,y:x*y, k,j))
# print(a)
#
# x = [1,2,3,4,5]
#
# def sq(lst):
#     f = []
#     for item in lst:
#         f.append(item*item)
#     return f
#
# print(sq(x))

listA = ["apple","banana","cherry"]
y = iter(listA)
print(next(y))
print(next(y))
print(next(y))
# print(next(y))

for item in listA:
    print(item)



