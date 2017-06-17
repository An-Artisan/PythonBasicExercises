import easygui as g
import  sys
# 打开文件的窗口，只显示.py的扩展名，返回选择的文件路径
file_name  = g.fileopenbox(default="./*py")
# 打开该文件，设置编码为UTF-8
file = open(file_name,'r',encoding='UTF-8')
# 显示在box中
g.textbox("你选择的文件内容为：","显示文件内容",text=file.readlines())
# 关闭文件
file.close()