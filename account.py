import easygui as g
import  sys
def account():
    easy_gui = g.multenterbox("【*真实姓名】为必填项。\n【*手机号码】为必填项。\n【*E-mail】为必填项。\n", "账号中心",
                              fields=("用户名", "*真实姓名", "固定电话", "*手机号码", "QQ", "*E-mail"))
    if (easy_gui[1] == '' and easy_gui[3] == '' and easy_gui[5] == ''):
        g.msgbox("带*的参数为必填，请重新输入！",ok_button="确定")
        account()
    sys.exit(0)
account()