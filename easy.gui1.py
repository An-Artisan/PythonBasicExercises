import easygui as g
import sys
#if g.ccbox():
#        pass         # user chose to continue
#else:
#        sys.exit(0)      # user chose to cancel
# choices = ['愿意', '不愿意', '有钱的时候愿意']
# reply = g.choicebox('你愿意购买资源打包支持小甲鱼吗？', choices = choices )
# g.msgbox(reply)
# g.buttonbox("图片显示~~","图片显示",image="sleep.gif",choices=("按钮1","按钮2"))
# print(g.diropenbox(default="."))
g.fileopenbox(default="E:\\Python\\PythonBasicExercises\\*.gif")