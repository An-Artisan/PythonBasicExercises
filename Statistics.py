import random
def count(*params):
    "用于统计输入的参数中有多少英文字符，数字字符，空格字符，以及其他字符的个数"

    #循环参数列表
    for i in range(0,len(params)):
        # 英文字符的个数置于0
        english_count = 0
        # 空格字符的个数置于0
        space_count = 0
        # 数字字符的个数置于0
        number_count = 0
        # 其他字符的个数置于0
        other_count = 0
        # 再次循环所有参数中的字符
        for j in range(0,len(params[i])):
            # 如果它的ASCII码小于9大于0就 数字统计变量+1
            if ord('9') > ord(params[i][j]) > ord('0'):
                number_count += 1
            # 如果它的ASCII码小于z大于a 或者 小于Z大于A 就 英文字符统计变量+1
            elif ord('a') > ord(params[i][j]) > ord('z') or ord('A') > ord(params[i][j]) > ord('Z'):
                english_count += 1
            # 如果它的ASCII码等于 空格，则空格统计变量+1
            elif ord(' ') == ord(params[i][j]):
                space_count += 1
            # 都不符合条件，代表是其他字符，则其他字符加1
            else:
                other_count += 1
        # 打印提示
        print("第",i,"个字符串共有：英语字母",english_count,"个，数字",number_count,"个，空格",space_count,"个，其他字符",other_count,"个")
# 打印函数说明
print(count.__doc__)
# 执行函数
count("1234","4 6")





