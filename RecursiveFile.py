import os
def RecursiveFile(dir):
    "递归目录并且打印"

    #打开目录并显示所有目录与文件
    list_dir = os.listdir(dir)
    # 循环所有目录和文件
    for list in list_dir:
        # 拼接路径
        filepath = os.path.join(dir, list)
        # 如果是目录则递归，是文件则打印
        if os.path.isdir(filepath):
            print("=========" + filepath + "========")
            # 开始递归
            RecursiveFile(filepath)
        else:
            # 打印文件名
            print("文件名为：" + list)
# 开始调用
RecursiveFile('./')
