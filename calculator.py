import re
import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from tkinter import Tk,E
from tkinter.ttk import Button,Label
from tkinter import StringVar, Entry,simpledialog,Text,Scrollbar
from math import pi, e, sin, cos, tan, log, log10, ceil, degrees, radians, exp, asin, acos, floor,sqrt,atan

import os
import tkinter.messagebox
import random


class calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('科学计算器')
        self.window.geometry("500x700")  # 设置窗口宽度为 300 个字符，高度为 200 个字符

        style = Style()
        style.configure('TButton', padding=5, font=('Arial', 15, 'bold'), relief='raised')
        style.configure('CButton', padding=5, font=('Arial', 8, 'bold'), relief='raised')
        self.string = StringVar()
        label = ttk.Label(self.window, textvariable=self.string, font=('Arial', 18) ,anchor=('e'))
        label.grid(row=0,pady=10,columnspan=5,sticky='e',ipady=20)


        ###################最顶端
        m = tkinter.Menu(self.window)
        self.window.config(menu=m)
        # 设置file选项
        filemenu = tkinter.Menu(m)
        m.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=lambda: self.callback('New'))
        filemenu.add_separator()
        filemenu.add_command(label="History", command=lambda: self.callback("History"))
        filemenu.add_separator()
        filemenu.add_command(label="Clear History", command=lambda: self.clear_history())  # 新增清空历史按钮
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: quit())
        filemenu.add_separator()
        filemenu.add_command(label="top", command=lambda: self.window.wm_attributes("-topmost", 1))
        filemenu.add_separator()

        # 设置help选项
        helpmenu = tkinter.Menu(m)
        m.add_cascade(label="Help", menu=helpmenu)
        self.list = ['π', 'e' , 'asin', '**', "√", "随机数"]
        list_explain = [" π:圆周率π的近似值", "e:自然对数e的近似值",
                        """asin,acos,atan,分别代表反三角函数：
        arcsin,arccos,arctan""", "÷:表示除号", "×:表示乘号,**：表示乘方",
                        "√:表示开方", "随机数：random.randint(x,y),将生成一个在区间[x,y]之间的随机整数"]
        index = 0
        self.help_dict = {}
        for i in self.list:
            helpmenu.add_command(label=i, command=lambda x=i: self.callback(x))
            self.help_dict[i] = list_explain[index]
            index += 1
        # 设置换算选项#
        changemenu = tkinter.Menu(m)
        m.add_cascade(label="换算", menu=changemenu)
        changemenu.add_command(label="BMI", command=lambda: self.callback("BMI"))
        changemenu.add_separator()
        changemenu.add_command(label="三维向量", command=lambda: self.callback("三维向量"))
        changemenu.add_separator()
        changemenu.add_command(label="信息1802抽签", command=lambda: self.callback("信息1802抽签"))




        self.value_1 = [" ","rad","sin","cos","tan",
                  "**","lg","ln","(",")",
                  "√","AC","Del","%","÷",
                  "x!","7","8","9","×",
                  "1/x","4","5","6","-",
                  "π","1","2","3","+",
                  "切换","e","0",".","="]
        self.value_2 = ["2nd","deg","sin","cos","tan",
                  "**","lg","ln","(",")",
                  "√","AC","Del","%","÷",
                  "x!","7","8","9","×",
                  "1/x","4","5","6","-",
                  "π","1","2","3","+",
                  "切换","e","0",".","="]
        self.value_3 = ["2nd", " ", "asin", "acos", "atan",
                        "**", "lg", "ln", "(", ")",
                        "√", "AC", "Del", "%", "÷",
                        "x!", "7", "8", "9", "×",
                        "1/x", "4", "5", "6", "-",
                        "π", "1", "2", "3", "+",
                        "切换", "e", "0", ".", "="]
        self.value_4 = [ "AC", "Del", "%", "÷",
                         "7", "8", "9", "×",
                         "4", "5", "6", "-",
                         "1", "2", "3", "+",
                         "切换", "0", ".", "="]
        self.mode_1 = 'rad'
        self.mode_2 = 1
        self.mode_3 = 1
        self.values = self.value_1
        self.button_generate(self.values)


        self.window.mainloop()

    def button_generate(self,values):
        ##################最低端
        btnHelp = Button(self.window, text="帮助", command=lambda: self.buttonClick("帮助"), width=5,
                         bootstyle="success")
        btnHelp.grid(row=8, column=0, padx=10, pady=10, ipady=8)
        btnQuit = Button(self.window, text="退出", command=lambda: quit(), width=5, bootstyle="success")
        btnQuit.grid(row=8, column=1, padx=10, pady=10, ipady=8)
        btnHelp = Button(self.window, text="历史", command=lambda: self.buttonClick("历史"), width=5,
                         bootstyle="success")
        btnHelp.grid(row=8, column=2, padx=10, pady=10, ipady=8)
        btnHelp = Button(self.window, text="randi", command=lambda: self.buttonClick("随机数"), width=5,
                         bootstyle="success")
        btnHelp.grid(row=8, column=3, padx=10, pady=10, ipady=8)
        btnHelp = Button(self.window, text=",", command=lambda: self.buttonClick(","), width=5,
                         bootstyle="success")
        btnHelp.grid(row=8, column=4, padx=10, pady=10, ipady=8)
        text = 1
        i = 0
        row = 1
        col = 0
        for txt in values:
            if (i == 5):
                row = 2
                col = 0
            if (i == 10):
                row = 3
                col = 0
            if (i == 15):
                row = 4
                col = 0
            if (i == 20):
                row = 5
                col = 0
            if (i == 25):
                row = 6
                col = 0
            if (i == 30):
                row = 7
                col = 0
            if self.string.get().startswith("."):
                self.string.set( "0" + self.string.get() + txt)
            if (txt == '='):

                btn = Button(self.window,text=txt,
                             command=lambda txt=txt: self.equals(),width=5,bootstyle="warning-TButton")
                btn.grid(column= col, row= row , padx=10, pady=10,ipady=8)                # btn.grid(row=row, column=col, padx=5, pady=5)


            elif (txt == 'Del'):
                btn = Button(self.window, text=txt,
                             command=lambda txt=txt: self.delete(),width=5,bootstyle = "warning-outline")
                btn.grid(column= col, row= row , padx=10, pady=10,ipady=8)                  # btn.grid(row=row, column=col, padx=5, pady=5)

            elif (txt == 'AC'):
                btn = Button(self.window, text=txt,
                             command=lambda txt=txt: self.clearall(),width=5,bootstyle="warning-outline")
                btn.grid(column= col, row= row , padx=10, pady=10,ipady=8)                   # btn.grid(row=row, column=col, padx=5, pady=5)

            elif (txt=="rad" or txt =="deg"):
                btn = Button(self.window,text=txt,
                             command=lambda txt=txt: self.switch_mode_1(),width=5,bootstyle = "light-TButton")

                btn.grid(column= col, row= row , padx=10, pady=10,ipady=8)

            elif (txt=="2nd"):
                btn = Button(self.window, text=txt,
                             command=lambda txt=txt: self.switch_mode_2(),width=5,bootstyle = "light-TButton")

                btn.grid(column= col, row= row , padx=10, pady=10,ipady=8)
            elif (txt=="切换"):
                btn = Button(self.window, text=txt,
                             command=lambda txt=txt: self.switch_mode_3(),width=5,bootstyle = "light-TButton")

                btn.grid(column= col, row= row , padx=10, pady=10,ipady=8)
            elif (txt=='%' or txt=='÷' or txt=='×' or txt=='-' or txt=='+'):
                n_txt = txt
                btn = Button(self.window, text=txt, command=lambda txt=n_txt: self.addChar(txt), width=5,
                             bootstyle="warning-outline")

                btn.grid(column=col, row=row, padx=10, pady=10,ipady=8)
            else:
                n_txt = txt
                if txt=='1/x':
                    n_txt = txt.replace("1/x", "**(-1)")
                if txt=='x!' :
                    n_txt = txt.replace("x!","!")
                if txt=='sin'or txt=='cos' or txt=='tan' or txt=='lg' or txt=='ln' or txt=="√" or txt=="asin" or txt=="acos" or txt=="atan":
                    n_txt = txt+'('
                btn = Button(self.window,text=txt,command=lambda txt=n_txt: self.addChar(txt),width=5,bootstyle = "light-TButton")

                btn.grid(column= col, row= row , padx=10, pady=10,ipady=8)


            col = col + 1
            i = i + 1
    def button_generate_2(self,values):
        ##################最低端
        btnHelp = Button(self.window, text="帮助", command=lambda: self.buttonClick("帮助"), width=7,
                         bootstyle="success-CButton")
        btnHelp.grid(row=6, column=0, padx=10, pady=10, ipady=20)
        btnQuit = Button(self.window, text="退出", command=lambda: quit(), width=7, bootstyle="success-CButton")
        btnQuit.grid(row=6, column=1, padx=10, pady=10, ipady=20)
        btnHelp = Button(self.window, text="历史", command=lambda: self.buttonClick("历史"), width=7,
                         bootstyle="success-CButton")
        btnHelp.grid(row=6, column=2, padx=10, pady=10, ipady=20)
        btnHelp = Button(self.window, text=",", command=lambda: self.buttonClick(","), width=7,
                         bootstyle="success-CButton")
        btnHelp.grid(row=6, column=3, padx=10, pady=10, ipady=20)
        text = 1
        i = 0
        row = 1
        col = 0
        for txt in values:
            if (i == 4):
                row = 2
                col = 0
            if (i == 8):
                row = 3
                col = 0
            if (i == 12):
                row = 4
                col = 0
            if (i == 16):
                row = 5
                col = 0
            if self.string.get().startswith("."):
                self.string.set( "0" + self.string.get() + txt)
            if (txt == '='):

                btn = Button(self.window,text=txt,
                             command=lambda txt=txt: self.equals(),width=7,bootstyle="warning-TButton")
                btn.grid(column= col, row= row , padx=10, pady=10,ipady=20)                # btn.grid(row=row, column=col, padx=5, pady=5)


            elif (txt == 'Del'):
                btn = Button(self.window, text=txt,
                             command=lambda txt=txt: self.delete(),width=7,bootstyle = "warning-outline")
                btn.grid(column= col, row= row , padx=10, pady=10,ipady=20)                  # btn.grid(row=row, column=col, padx=5, pady=5)

            elif (txt == 'AC'):
                btn = Button(self.window, text=txt,
                             command=lambda txt=txt: self.clearall(),width=7,bootstyle="warning-outline")
                btn.grid(column= col, row= row , padx=10, pady=10,ipady=20)                   # btn.grid(row=row, column=col, padx=5, pady=5)

            elif (txt=="rad" or txt =="deg"):
                btn = Button(self.window,text=txt,
                             command=lambda txt=txt: self.switch_mode_1(),width=7,bootstyle = "light-TButton")

                btn.grid(column= col, row= row , padx=10, pady=10,ipady=20)

            elif (txt=="2nd"):
                btn = Button(self.window, text=txt,
                             command=lambda txt=txt: self.switch_mode_2(),width=7,bootstyle = "light-TButton")

                btn.grid(column= col, row= row , padx=10, pady=10,ipady=20)
            elif (txt=="切换"):
                btn = Button(self.window, text=txt,
                             command=lambda txt=txt: self.switch_mode_3(),width=7,bootstyle = "light-TButton")

                btn.grid(column= col, row= row , padx=10, pady=10,ipady=20)
            elif (txt=='%' or txt=='÷' or txt=='×' or txt=='-' or txt=='+'):
                n_txt = txt
                btn = Button(self.window, text=txt, command=lambda txt=n_txt: self.addChar(txt), width=7,
                             bootstyle="warning-outline")

                btn.grid(column=col, row=row, padx=10, pady=10,ipady=20)
            else:
                n_txt = txt
                if txt=='1/x':
                    n_txt = txt.replace("1/x", "**(-1)")
                if txt=='x!' :
                    n_txt = txt.replace("x!","!")
                if txt=='sin'or txt=='cos' or txt=='tan' or txt=='lg' or txt=='ln' or txt=="√" or txt=="asin" or txt=="acos" or txt=="atan":
                    n_txt = txt+'('

                btn = Button(self.window,text=txt,command=lambda txt=n_txt: self.addChar(txt),width=7,bootstyle = "light-TButton")

                btn.grid(column= col, row= row , padx=10, pady=10,ipady=20)


            col = col + 1
            i = i + 1
    def switch_mode_1(self):
        # 切换模式
        self.mode_1 = "deg" if self.mode_1 == "rad" else "rad"
        # 根据模式选择相应的值
        self.values = self.value_2 if self.mode_1 == "deg" else self.value_1

        self.button_generate(self.values)

    def switch_mode_2(self):
        # 切换模式
        self.mode_2 = -1 if self.mode_2 == 1 else 1
        # 根据模式选择相应的值
        self.values = self.value_3 if self.mode_2 == -1 else self.value_2

        self.button_generate(self.values)
    def switch_mode_3(self):
        for widget in self.window.winfo_children():
            # 判断子组件是否为按钮
            if isinstance(widget, ttk.Button):
                # 销毁按钮
                print('!')
                widget.destroy()
        # 切换模式
        self.mode_3 = 0 if self.mode_3 == 1 else 1
        # 根据模式选择相应的值
        self.values = self.value_4 if self.mode_3 == 0 else self.value_1

        self.button_generate_2(self.values) if self.mode_3 ==0 else self.button_generate(self.values)
    def clearall(self):
        self.string.set("")

    def equals(self):
        result = ""
        flag = 0
        # 读取文件位置
        pdw = os.getcwd()
        outfile = open(pdw + "\\history.txt", "a")
        outfile.write(self.string.get())
        #获取字符串，与正则匹配数字
        new_string = self.string.get()
        match = re.search(r'(\d+)!', new_string)
        match_2 = re.search(r'ln\((\d+)\)', new_string)


        if "×" in new_string:
            new_string = new_string.replace("×", "*")
        if "÷" in new_string:
            new_string = new_string.replace("÷",'/')
        if "√" in new_string:
            new_string = new_string.replace("√","sqrt")
        if "!" in new_string:
            print(new_string)
            number = match.group(1)
            new_string = new_string.replace(match.group(), f'self.stage_by({number})')
        if "lg" in new_string:
            new_string = new_string.replace("lg","log10")
        if "ln" in new_string:
            print(new_string)
            number = match_2.group(1)
            new_string = new_string.replace(match_2.group(),f"log({number},e)")
        if "π" in new_string:
            new_string = new_string.replace("π", "pi")
            print(new_string)
        if self.mode_2==-1:
            if "asin" in new_string or "acos" in new_string or "atan" in new_string:
                match_6 = re.search(r'(asin|acos|atan)\((\d+(\.\d+)?)\)', self.string.get())
                number = match_6.group(0)
                new_string = new_string.replace(match_6.group(),f'degrees({number})')
                flag = 1
        else:
            if self.mode_1=='deg':
                if "sin" in new_string:
                    match_3_int = re.search(r'sin\((\d+)(\.\d+)°\)', new_string)
                    match_3_f= re.search(r'sin\(\d+(\.\d+)°\)', new_string)
                    number = match_3_int.group(1)+match_3_f.group(1)
                    print(number)
                    new_string = new_string.replace(new_string, f"sin({radians(float(number))})")

                if "cos" in new_string:
                    match_4_int = re.search(r'sin\((\d+)(\.\d+)°\)', new_string)
                    match_4_f = re.search(r'sin\(\d+(\.\d+)°\)', new_string)
                    number = match_4_int.group(1) + match_4_f.group(1)
                    new_string = new_string.replace(new_string, f"sin({radians(float(number))})")

                if "tan" in new_string:
                    match_5_int = re.search(r'sin\((\d+)(\.\d+)°\)', new_string)
                    match_5_f = re.search(r'sin\(\d+(\.\d+)°\)', new_string)
                    number = match_5_int.group(1) + match_5_f.group(1)
                    new_string = new_string.replace(new_string, f"sin({radians(float(number))})")

        try:
            result = str(eval(new_string))

            if flag == 1:
                result = result+'°'
            self.string.set(result)
        except:
            result = "INVALID INPUT"
        self.string.set(result)
        #写入到文件
        outfile.write("=" + str(result) + "\n")
        outfile.close()

    def addChar(self, char):
        if self.mode_1=='deg' and len(self.string.get()) and self.mode_2!=-1:
            match = re.search(r'(sin|cos|tan)\((\d*\.?\d+)\)', self.string.get())
            print(match.group())
            if char in ('0','1','2','3','4','5','6','7','8','9') and match and self.string.get()[-1]!='°':
                self.string.set(self.string.get() + (str(char))+'°')

            elif self.string.get()[-1]=='°' and char in ('0','1','2','3','4','5','6','7','8','9'):
                self.string.set(self.string.get()[0:-1]+(str(char))+'°')
            elif self.string.get()[-1]=='°' and char =='.':
                self.string.set(self.string.get()[0:-1]+(str(char)))
            else:
                self.string.set(self.string.get() + (str(char)))
        else:
            self.string.set(self.string.get() + (str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])
    def stage_by(self,x):
        temp = 1
        for j in range(1, x + 1):
            temp = temp*j
        return temp

    def buttonClick(self,btn):
        # 获取录入框中的文本内容
        content = self.string.get()
        # 根据不同的按钮，做出相应的处理
        # 如果已有内容时以小数点开头的，前面加0
        # 如果参数为Clear,清空文本框，如果参数为Del,去除最后一个字符

        if btn == "帮助":
            tkinter.messagebox.showinfo("帮助", """     pi:圆周率π的近似值
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
            try:
                pdw = os.getcwd()
                infile = open(pdw + "\\history.txt", "r")
                text = infile.read()
                infile.close()

                tkinter.messagebox.showinfo("历史", text)
            except FileNotFoundError:
                tkinter.messagebox.showerror("历史", "历史文件不存在")
            return

        elif btn == "随机数":
            content += "random.randint("
        elif btn in self.values:
            if content.endswith(self.values):
                tkinter.messagebox.showerror("错误", "不允许连续运算符")
                return
            content += btn
        elif btn == ',':
            content = content+','
        self.string.set(content)

    def clear_history(self):
        pdw = os.getcwd()
        history_file_path = pdw + "\\history.txt"

        # 删除历史文件内容
        with open(history_file_path, 'w') as history_file:
            history_file.write('')
        text = "历史已清空"
        tkinter.messagebox.showinfo('提示',text)
    ##################################文件顶端
    def callback(self,btn):
        content = self.string.get()
        if btn == "New":
            content = ""
        elif btn == "History":
            pdw = os.getcwd()
            print(pdw)
            try:
                infile = open(pdw + "\history.txt", "r")
            except:
                tkinter.messagebox.showerror("不存在历史")
            text = infile.read()
            infile.close()
            tkinter.messagebox.showinfo("历史", text)
            return
        elif btn in self.list:
            tkinter.messagebox.showinfo("Help", self.help_dict[btn])
            return
        elif btn == "BMI":
            window_BMI = tk.Toplevel()
            window_BMI.geometry("350x200")
            window_BMI.title("这是一个计算BMI的程序")

            height = tk.StringVar()
            tk.Label(window_BMI, text="请输入身高（米）：").place(x=10, y=10)
            tk.Entry(window_BMI, textvariable=height).place(x=150, y=10)

            weight = tk.StringVar()
            tk.Label(window_BMI, text="请输入体重（千克）：").place(x=10, y=50)
            tk.Entry(window_BMI, textvariable=weight).place(x=150, y=50)
            btnBMI = tk.Button(window_BMI, text="计算", command=lambda: BMI())
            btnBMI.place(x=10, y=90, height=30, width=50)

            out_BMI = tk.StringVar()
            tk.Label(window_BMI, text="BMI指数：").place(x=10, y=130)
            tk.Entry(window_BMI, textvariable=out_BMI).place(x=150, y=130)
            out_standard = tk.StringVar()
            tk.Label(window_BMI, text="指标水平：").place(x=10, y=170)
            tk.Entry(window_BMI, textvariable=out_standard).place(x=150, y=170)

            def BMI():
                new_height = float(height.get())
                new_weight = float(weight.get())
                BMI = round(new_weight / new_height ** 2, 2)
                out_BMI.set('BMI:'+str(BMI))
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
            window_vector = tk.Toplevel(self.window)
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

            # 定义一个三维向量的类(重载运算符）
            # 让类拦截常规的Python运算，重载是通过特殊名称的类方法来实现的
            # 运算符重载只是意味着在类方法中拦截内置的操作——
            # 当类的实例出现在内置操作中，Python自动调用你的方法，
            # 并且你的方法的返回值变成了相应操作的结果。
            class Vector3:
                def __init__(self, x, y, z):
                    self.x = x
                    self.y = y
                    self.z = z

                # 重载 +,-,*,**
                def __add__(self, obj):
                    return Vector3(self.x + obj.x, self.y + obj.y, self.z + obj.z)

                def __sub__(self, obj):
                    return Vector3(self.x - obj.x, self.y - obj.y, self.z - obj.z)

                def __mul__(self, obj):
                    return Vector3(self.x * obj.x, self.y * obj.y, self.z * obj.z)

                def __str__(self):
                    return str(self.x) + "," + str(self.y) + "," + str(self.z)

                # 向量的外积，(x1,y1,z1) x (x2,y2,z2)=(y1z2 - y2z1,z1x2-z2x1,x1y2-x2y1)
                def __pow__(self, obj):
                    return Vector3(self.y * obj.z - obj.y * self.z,
                                   self.z * obj.x - obj.z * self.x, self.x * obj.y - obj.x * self.y)

            def vector():
                try:
                    v1 = vector1.get()
                    v2 = vector2.get()
                    l = re.split(",", v1) + re.split(",", v2)
                    print(l)
                    x, y, z, m, n, l = int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5])
                except:
                    tkinter.messagebox.showerror("错误", "输入错误")

                V1 = Vector3(x, y, z)
                V2 = Vector3(m, n, l)
                out_add = tk.StringVar()
                tk.Label(window_vector, text=" v1 + v2 = ").place(x=10, y=180)
                tk.Entry(window_vector, textvariable=out_add).place(x=100, y=180)
                out_add.set(V1 + V2)
                out_sub = tk.StringVar()
                tk.Label(window_vector, text=" v1 - v2 = ").place(x=10, y=240)
                tk.Entry(window_vector, textvariable=out_sub).place(x=100, y=240)
                out_sub.set(V1 - V2)
                out_mul = tk.StringVar()
                tk.Label(window_vector, text="内积：v1.v2=").place(x=10, y=300)
                tk.Entry(window_vector, textvariable=out_mul).place(x=100, y=300)
                out_mul.set(V1 * V2)
                out_pow = tk.StringVar()
                tk.Label(window_vector, text="外积：v1Xv2=").place(x=10, y=350)
                tk.Entry(window_vector, textvariable=out_pow).place(x=100, y=350)
                out_pow.set(V1 ** V2)

        elif btn == "信息1802抽签":
            window_select = tk.Toplevel(self.window)
            window_select.geometry("350x400")
            window_select.title("信息1802抽签")

            get_number = tk.StringVar()
            tk.Label(window_select, text="请输入人数:0~32").place(x=10, y=10)
            tk.Entry(window_select, textvariable=get_number).place(x=100, y=40)
            lists = ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10\n', '11\n', '12\n', '13\n',
                     '14\n', '15\n', '16\n', '17\n', '18\n', '19\n', '20\n', '21\n', '22\n', '23\n', '24\n', '25\n',
                     '26\n', '27\n', '28\n', '29\n', '30\n', '31\n', '32\n']


            def what_number():
                content = ''
                number = int(get_number.get())
                if number < 0 or number > 32:
                    content = "输入错误！"
                else:
                    for i in range(1, number + 1):
                        x = random.randint(1, len(lists)) - 1
                        content += lists[x] + "\n"

                # 清空 Text 控件内容
                out_numbers.delete(1.0, tk.END)
                # 在 Text 控件中插入新内容
                out_numbers.insert(tk.END, content)

            btn_number = tk.Button(window_select, text="抽取", command=what_number, height=2)
            btn_number.place(x=10, y=120, height=30, width=50)

            # 创建一个带有滚动条的 Text 控件
            out_numbers = Text(window_select, wrap=tk.WORD, height=10, width=30)
            out_numbers.place(x=10, y=160)
            scrollbar = Scrollbar(window_select, command=out_numbers.yview)
            scrollbar.place(x=285, y=160, height=180)
            out_numbers.config(yscrollcommand=scrollbar.set)


        self.string.set(content)

calculator()
