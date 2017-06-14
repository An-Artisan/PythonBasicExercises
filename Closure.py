def funX():
    x = 5
    def funY():
        nonlocal x
        x += 1
        return x
    return funY

a = funX()
print(a())
print(a())
print(a())
# 会打印
# 6
# 7
# 8
# 当 a= funX()的时候，只要a变量没有被重新复制，funX()就没有被释放，也就是说局部变量X就没有被重新初始化
# 当全局变量不适用的时候，可以考虑使用闭包，更安全和更稳定