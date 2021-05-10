w = 'AAAAAAAAABBBBBBBBBEEEEEEEEEEEIIIIIIOOOOUUUUUaaaaaooiiieeeuuu'
a = sorted(set(w))
print(a)

b = 'aeiouAEIOU'
count = 0
for char in a:
    if char in b:
        count = count + 1
print(count)
for char in a:
    if char in b:
        print(char, w.count(char))







