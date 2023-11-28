#计算器

#第一部分——导入库和库函数

import os
import re
import tkinter as tk
import random
import tkinter.messagebox
from math import *


#第二部分——对窗口、文本框的设置

#建新窗口—根窗口
root = tkinter.Tk()
#设置窗口的大小和位置
root.geometry("300x490+400+200")
#不允许改变高，不允许改变宽,0或False均可
root.resizable(0,False)
#设置窗口标题
root.title("计算器")
#在根窗口中建新一个以contentVar为控制变量的文本框，类型为可变文本框
contentVar = tkinter.StringVar(root,"")
# tkinter中，Entry表示单行文本框，Text表示多行文本框
# 用textvariable设置为可变文本，与StringVar可变文本框等配合使用
contentEntry = tkinter.Entry(root,textvariable = contentVar)
#将文本框状态设置为正常，即允许在文本框中进行键盘输入
contentEntry["state"] = "normal"
#设置文本框的位置，宽度和高度
contentEntry.place(x=10,y=10,width=280,height=20)


#第三部分——放置菜单和按钮

#（1）第一小部分放置按钮

#放置清除按钮和等号按钮,帮助与退出按钮
#传递给command属性的是函数对象，函数名后不能加括号,而这样定义的函数不能传递参数，
#而执行相应的操作，需要对不同参数进行处理，故需要重新定义一个函数，让这个函数调用另一个函数
#lambda是一种快速定义的最小函数（单行）
#注意:lambda 函数可以接收任意多个参数 (包括可选参数),并且返回单个表达式的值。
#lambda 函数不能包含命令，包含的表达式不能超过一个。
btnClear = tkinter.Button(root,text="Clear",command=lambda:buttonClick("Clear"))
btnClear.place(x=20,y=40,width=50,height=20)
btnDel = tkinter.Button(root,text="Del",command=lambda:buttonClick("Del"))
btnDel.place(x=90,y=40,width=50,height=20)
btnCompute = tkinter.Button(root,text="=",command=lambda:buttonClick("="))
btnCompute.place(x=230,y=40,width=50,height=20)
btnHelp = tkinter.Button(root,text="帮助",command=lambda:buttonClick("帮助"))
btnHelp.place(x=230,y=350,width=50,height=50)
btnQuit = tkinter.Button(root,text="退出",command=lambda:quit())
btnQuit.place(x=230,y=430,width=50,height=20)

#放置()[]按钮
signs = ["(",")","[","]"]
number = 0
for sign in signs:
    number += 1
    btnDigist = tkinter.Button(root,text=sign,command=lambda x=sign:buttonClick(x))
    btnDigist.place(x=155+15*number,y=40,width=14,height=20)
    
#放置0123456789十个数字，小数点，计算平方根,调用三角反三角函数以及随机数和历史的按钮
digists = list("0123456789.") + ["sqrt(","sin(","cos(","tanx(","asin(","acos(",
                                 "atan(","ceil(","floor(","abs(",",","随机数","历史"] 
index = 0
for row in range(8):
    for col in range(3):
        d = digists[index]
        index += 1
        btnDigist = tkinter.Button(root,text=d,command=lambda x=d:buttonClick(x))
        btnDigist.place(x=20 + col*70,y=80 + row*50,width = 50,height = 20)

#放置运算符按钮和π，e以及数学常数τ的近似值按钮
operators = ("+","-","*","/","**","//","pi","e","tau")
for index,operator in enumerate(operators):
    btnOperator = tkinter.Button(root,text=operator,command=lambda x=operator:buttonClick(x))
    btnOperator.place(x=230,y=80+index*30,width=50,height=20)

#（2）第二小部分放置菜单
    
m = tkinter.Menu(root)
root.config(menu=m)
#设置file选项
filemenu = tkinter.Menu(m)
m.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command = lambda: callback("New"))
filemenu.add_separator()
filemenu.add_command(label="History",command=lambda:callback("History"))
filemenu.add_separator()
filemenu.add_command(label="Exit",command=lambda:quit())
filemenu.add_separator()
filemenu.add_command(label="top",command=lambda:root.wm_attributes("-topmost",1))
filemenu.add_separator()

#设置help选项
helpmenu = tkinter.Menu(m)
m.add_cascade(label="Help",menu=helpmenu)
list=['pi','e','tau','asin','//','**',"sqrt函数","随机数"]
list_explain=["pi:圆周率π的近似值","e:自然对数e的近似值",'tau:数学常数τ的近似值',
              """asin,acos,atan,分别代表反三角函数：
arcsin,arccos,arctan""","/:表示除号,//:表示整除","*:表示乘号,**：表示乘方",
              "Sqrt:表示开方","随机数：random.randint(x,y),将生成一个在区间[x,y]之间的随机整数"]
index=0
help_dict={}
for i in list:
    helpmenu.add_command(label=i,command=lambda x=i:callback(x))
    help_dict[i]=list_explain[index]
    index += 1
#设置换算选项#
changemenu=tkinter.Menu(m)
m.add_cascade(label="换算",menu=changemenu)
changemenu.add_command(label="BMI",command=lambda:callback("BMI"))
changemenu.add_separator()
changemenu.add_command(label="三维向量",command=lambda:callback("三维向量"))
changemenu.add_separator()
changemenu.add_command(label="信息1802抽签",command=lambda:callback("信息1802抽签"))


#第四部分——按钮处理代码和菜单处理代码
    
#(1)第一小部分按钮处理代码

def buttonClick(btn):
    #获取录入框中的文本内容
    content = contentVar.get()
    #根据不同的按钮，做出相应的处理
    #如果已有内容时以小数点开头的，前面加0
    if content.startswith("."):
        content = "0" + content + btn
    #如果参数为Clear,清空文本框，如果参数为Del,去除最后一个字符
    elif btn == "Clear":
        content = ""
    elif btn == "Del":
        content = content[:-1]
    #如果新输入字符串btn是小数点，且字符串content的个数大于1并以运算符结尾时，
    #在小数点前加0,以数字结尾时，添加小数点，以ieu,结尾时报错，不对文本框内容做修改
    elif btn == "." and len(content) >= 1:
        if content[-1] in "()[]+-*/":
            content = content + "0."
        elif content[-1] in "0123456789":
            content += btn
        elif content[-1] in "ieu,":
            tkinter.messagebox.showerror("错误：","π,eτ后不能有小数点")
            return
    #如果参数在"0123456789,()[]sin(cos(tan(pietauasin(acos(atan(ceil(floor(abs("之中，
    #在文本框末尾直接加入此参数
    elif btn in "0123456789,()[]sin(cos(tan(pietauasin(acos(atan(ceil(floor(abs(":
        content += btn
    #如果参数为帮助，则弹出帮助提示界面,内含相关按钮介绍及使用方法
    elif btn == "帮助":
        tkinter.messagebox.showinfo("帮助","""    pi:圆周率π的近似值
    e:自然对数e的近似值
    tau:数学常数τ的近似值
    asin,acos,atan,分别代表反三角函数：
        arcsin,arccos,arctan
    /:表示除号
    //:表示整除
    *:表示乘号
    **：表示乘方
    Sqrt:表示开方
    Clear:表示清空数据
    del：表示退格，相当于电脑上的Backsace键
    随机数：random.randint(x,y),将生成一个在区间[x,y]之间的随机整数
    其他问题以及改进意见，请加QQ：273983336""")
    elif btn == "历史":
        pdw = os.getcwd()
        infile = open(pdw + "\\history.txt","r")
        text = infile.read()
        infile.close()
        tkinter.messagebox.showinfo("历史",text)
        return
    elif btn=="随机数":
        content += "random.randint("
    elif btn == "=":
        try:
            #对输入的表达式求值,并写入文件
            #获取当前文件所在的路径
            pdw = os.getcwd()
            outfile = open(pdw + "\\history.txt","a")
            outfile.write(content)
            content = str(round(eval(content),10))
            outfile.write("=" + content + "\n")
            outfile.close()
        except:
            tkinter.messagebox.showerror("错误","表达式错误")
            outfile.write("\n")
            return 
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror("错误","不允许连续运算符")
            return
        content += btn
    #如果参数为Sqrt,则
    elif btn == "sqrt(":
        try:
            content += "sqrt("
            #content = eval(content) ** 0.5
        except:
            tkinter.messagebox.showerror("错误","表达式错误")
    contentVar.set(content)

#(2)第二小部分菜单处理代码
    
def callback(btn):
    content = contentVar.get()
    if btn == "New":
        content = ""
    elif btn == "History":
        pdw = os.getcwd()
        infile = open(pdw + "\\history.txt","r")
        text = infile.read()
        infile.close()
        tkinter.messagebox.showinfo("历史",text)
        return
    elif btn in list:
        tkinter.messagebox.showinfo("Help",help_dict[btn])
        return
    elif btn == "BMI":
        window_BMI=tk.Toplevel(root)
        window_BMI.geometry("350x200")
        window_BMI.title("这是一个计算BMI的程序")
    
        height=tk.StringVar()
        tk.Label(window_BMI,text="请输入身高（米）：").place(x=10,y=10)
        tk.Entry(window_BMI,textvariable=height).place(x=150,y=10)
    
        weight=tk.StringVar()
        tk.Label(window_BMI,text="请输入体重（千克）：").place(x=10,y=50)
        tk.Entry(window_BMI,textvariable=weight).place(x=150,y=50)
        btnBMI = tk.Button(window_BMI,text="计算",command=lambda:BMI())
        btnBMI.place(x=10,y=90,height=30,width=50)
        
        out_BMI=tk.StringVar()
        tk.Label(window_BMI,text="BMI指数：").place(x=10,y=130)
        tk.Entry(window_BMI,textvariable=out_BMI).place(x=150,y=130)
        out_standard=tk.StringVar()
        tk.Label(window_BMI,text="指标水平：").place(x=10,y=170)
        tk.Entry(window_BMI,textvariable=out_standard).place(x=150,y=170)

        def BMI():
            new_height=float(height.get())
            new_weight=float(weight.get())
            BMI = round(new_weight / new_height ** 2 ,2)
            out_BMI.set(BMI)
            if BMI <= 18.5:
                out_standard.set("过轻")
            elif BMI > 18.5 and BMI <= 24:
                out_standard.set("健康")
            elif BMI > 24 and BMI <= 28:
                out_standard.set("过重")
            elif BMI > 28 and BMI <= 32:
                out_standard.set("肥胖")
            else:
                out_standard.set("重度肥胖")
    elif btn == "三维向量":
        window_vector=tk.Toplevel(root)
        window_vector.geometry("350x400")
        window_vector.title("三维向量的运算")

        vector1 = tk.StringVar()
        tk.Label(window_vector, text="请输入向量v=(x,y,z)形如x,y,z,逗号为英文输入法下的逗号").place(x=10, y=10)
        tk.Label(window_vector, text="例如：v=1,1,1").place(x=10, y=30)
        tk.Label(window_vector, text="V1=").place(x=20, y=60)
        tk.Entry(window_vector, textvariable=vector1).place(x=100, y=60)

        vector2 = tk.StringVar()
        tk.Label(window_vector, text="V2=").place(x=20, y=100)
        tk.Entry(window_vector, textvariable=vector2).place(x=100, y=100)

        btnvector = tk.Button(window_vector, text="计算", command=lambda: vector())
        btnvector.place(x=10, y=140, height=30, width=50)

        
        #定义一个三维向量的类(重载运算符）
        #让类拦截常规的Python运算，重载是通过特殊名称的类方法来实现的
        #运算符重载只是意味着在类方法中拦截内置的操作——
        #当类的实例出现在内置操作中，Python自动调用你的方法，
        #并且你的方法的返回值变成了相应操作的结果。
        class Vector3:
            def __init__(self,x,y,z):
                self.x=x
                self.y=y
                self.z=z
            #重载 +,-,*,**
            def __add__(self,obj):
                return Vector3(self.x + obj.x,self.y + obj.y,self.z + obj.z)
            def __sub__(self,obj):
                return Vector3(self.x - obj.x,self.y - obj.y,self.z - obj.z)
            def __mul__(self,obj):
                return Vector3(self.x * obj.x,self.y * obj.y,self.z * obj.z)
            def __str__(self):
                return str(self.x) + "," + str(self.y) + "," + str(self.z)
            # 向量的外积，(x1,y1,z1) x (x2,y2,z2)=(y1z2 - y2z1,z1x2-z2x1,x1y2-x2y1)
            def __pow__(self,obj):
                return Vector3(self.y*obj.z - obj.y*self.z,
                            self.z*obj.x - obj.z*self.x,self.x*obj.y - obj.x*self.y)

        def vector():
            try:
                v1=vector1.get()
                v2=vector2.get()
                l=re.split(",",v1)+re.split(",",v2)
                print(l)
                x,y,z,m,n,l=int(l[0]),int(l[1]),int(l[2]),int(l[3]),int(l[4]),int(l[5])
            except:
                tkinter.messagebox.showerror("错误","输入错误")
                
            V1=Vector3(x,y,z)
            V2=Vector3(m,n,l)
            out_add=tk.StringVar()
            tk.Label(window_vector,text=" v1 + v2 = ").place(x=10,y=180)
            tk.Entry(window_vector,textvariable=out_add).place(x=100,y=180)
            out_add.set(V1+V2)
            out_sub=tk.StringVar()
            tk.Label(window_vector,text=" v1 - v2 = ").place(x=10,y=240)
            tk.Entry(window_vector,textvariable=out_sub).place(x=100,y=240)
            out_sub.set(V1-V2)
            out_mul=tk.StringVar()
            tk.Label(window_vector,text="内积：v1.v2=").place(x=10,y=300)
            tk.Entry(window_vector,textvariable=out_mul).place(x=100,y=300)
            out_mul.set(V1*V2)
            out_pow=tk.StringVar()
            tk.Label(window_vector,text="外积：v1Xv2=").place(x=10,y=350)
            tk.Entry(window_vector,textvariable=out_pow).place(x=100,y=350)
            out_pow.set(V1**V2)
            
    elif btn == "信息1802抽签":
        window_select = tk.Toplevel(root)
        window_select.geometry("350x400")
        window_select.title("信息1802抽签")

        get_number = tk.StringVar()
        tk.Label(window_select,text="请输入人数:0~32").place(x=10,y=10)
        tk.Entry(window_select,textvariable=get_number).place(x=100,y=40)
        lists=['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10\n', '11\n', '12\n', '13\n', '14\n', '15\n', '16\n', '17\n', '18\n', '19\n', '20\n', '21\n', '22\n', '23\n', '24\n', '25\n', '26\n', '27\n', '28\n', '29\n', '30\n', '31\n', '32\n']

        btnnumber = tk.Button(window_select,text="抽取",command=lambda:what_number())
        btnnumber.place(x=10,y=120,height=30,width=50)

        def what_number():
            content=''
            number=int(get_number.get())
            if number<0 or number >32:
                content = "输入错误！"
            else:
                for i in range(1,number+1):
                    x=random.randint(1,len(lists))-1
                    content += lists[x] + " "
            out_numbers=tk.StringVar()
            tk.Entry(window_select,textvariable=out_numbers).place(x=10,y=250,width=280,height=20)
            
            out_numbers.set(content)

                
                
        
    contentVar.set(content)


    
#第五部分——进入主循环
    
#进入主（消息）循环，准备处理事件（必须组建），除非用户关闭窗口（或者按退出键），
#否则程序将一直处于主循环中
#注意：只有进入了主循环，根窗口才可见
root.mainloop()




