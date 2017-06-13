import  random
#设置一个死循环
while True :
    # 接受用户输入的字符串
    Palind = input("请输入字符串：")
    # 定义个空字符串变量
    Palind_new = ''
    # for循环用户输入的字符串，开始为字符串的长度减一，结束为-1，步长为-1
    for i in range(len(Palind)-1,-1,-1) :
        # 加赋值这个新变量中
        Palind_new += Palind[i]
    # 如果相等，代表是回文串
    if Palind == Palind_new :
        # 打印提示用户信息，并跳出循环
        print("恭喜你，你输入的字符是回文联")
        break
    else :
        # 打印用户信息，并结束本次循环
        print("对不起，你输入的字符不是回文联")
        continue
