def da(basic):
    da = basic * 0.8
    return da

def hra(basic):
    hra = basic * 0.15
    return hra

def pf(basic):
    pf = basic * 0.12
    return pf

def itax(gross):
    tax = gross * 0.10
    return tax


if __name__ == '__main__':
    print(hra(12000))
    print(__name__)
    print('Running from the original file')

else:
    print(__name__)
    print('call from the another programmmmm')

#
# basicSalary = float(input("enter basic salary"))
#
# grossSal = basicSalary + da(basicSalary) + hra(basicSalary)
# netSal = grossSal - pf(basicSalary) - itax(grossSal)
#
# print(f"my net salary is {netSal} and gross salary is {grossSal}")


