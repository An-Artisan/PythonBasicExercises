class C:
    count = 0

    def __init__(self):
        C.count += 1

    def __del__(self):
        C.count -= 1

a = C()
b = C()
c = C()
print(C.count)
del a
del b, c
print(C.count)
