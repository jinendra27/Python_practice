class a:
    n = 0
    def __init__(self):
        a.n += 1

    @staticmethod
    def count():
        print(a.n)


A = a()
B = a()
C = a()
D = a()

a.count()









