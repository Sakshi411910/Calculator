import tkinter as tk
import math
#Creating window
window = tk.Tk()
window.title("Scientific calculator")
window.maxsize(1000, 1000)
window.minsize(340,500)

ans = tk.StringVar()
#Creating Entries
display = tk.Entry(window, font=('Times New Roman', 40), bg='black', fg='white', width=35, justify='right',
                      textvariable=ans)
display.grid(row=1, column=0, columnspan=8)

display_2=tk.Entry(window, textvariable="",width=56,bg='#d1dbe4',fg='#393939',
                    font=('Times New Roman',25), justify='right')
display_2.grid(row=0,column=0,columnspan=8 )

#Function definitions for all buttons
def click(btn):
    e = display.get()
    if btn == "AC":
        display_2.delete(0, tk.END)
        ans.set(" ")
    elif btn == "C":
        display_2.delete(0, "end")
        ans.set(e[:-1])
    elif btn == "√":
        display_2.insert("end","√"+e)
        if(float(eval(e))<0):
            ans.set("undefined")
        else:
            ans.set(math.sqrt(eval(e)))
    elif btn == "=":                                                                                              
        display_2.insert("end",e)
        if e[-2:]=="/0":
            ans.set("undefined")
        else:
            ans.set(eval(e))
    elif btn == "π":
        ans.set(math.pi)
    elif btn == "2π":
        ans.set(math.pi * 2)
    elif btn == "sin":
        display_2.insert("end","sin("+e)
        if (float(eval(e))%180 == 0):
            ans.set("0")
        else:
            ans.set(math.sin(math.radians(eval(e))))
        display_2.insert("end",")")
    elif btn == "cos":
        display_2.insert("end","cos("+e)
        if (float(eval(e))%90==0 and float(eval(e))%180!=0):
            ans.set("0")
        else:
            ans.set(math.cos(math.radians(eval(e))))
        display_2.insert("end",")")
    elif btn == "tan":
        display_2.insert("end","tan("+e)
        if (float(eval(e))%90==0 and float(eval(e))%180!=0):
            ans.set("undefined")
        elif(float(eval(e))%180 == 0):
            ans.set("0")
        else:
            ans.set(math.tan(math.radians(eval(e))))
        display_2.insert("end",")")
    elif btn == "arcsin":
        if -1<=+float(e)<=1:
            display_2.insert("end","arcsin("+e+")")
            ans.set(math.degrees(math.asin(eval(e))))
        else:
            display_2.insert("end","domain error")
    elif btn == "arccos":
        if -1<+int(e)<=1:
            display_2.insert("end","arccos("+e+")")
            ans.set(math.degrees(math.acos(eval(e))))
        else:
            display_2.insert("end","domain error")
    elif btn == "arctan":
        display_2.insert("end","arctan("+e+")")
        ans.set(math.degrees(math.atan(eval(e))))
    elif btn == "x^y":
        display.insert("end", "**")
    elif btn == "1/x":
        display_2.insert("end","1/"+e)
        if eval(e)==0:
            ans.set("undefined")
        else:
            ans.set(1 / float(eval(e)))
    elif btn == "^2":
        display_2.insert("end",e+"^2")
        ans.set(float(eval(e)) ** 2)
    elif btn == "ln":
        display_2.insert("end","ln("+e+")")
        ans.set(math.log(eval(e)))
    elif btn == "deg":
        ans.set(math.degrees(eval(e)))
    elif btn == "rad":
        ans.set(math.radians(eval(e)))
    elif btn == "e":
        display_2.insert("end","e")
        ans.set(math.e)
    elif btn == "log10":
        display_2.insert("end","lg("+e+")")
        ans.set(math.log10(eval(e)))
    elif btn == "10^x":
        display_2.insert("end","10^"+e)
        if eval(e)>300:
            ans.set("out of range")
        else:
            ans.set(10 ** float(eval(e)))
    elif btn == "x!":
        display_2.insert("end",e+"!"+"=")
        if eval(e)>10000:
            ans.set("out of range")
        else:
            ans.set(math.factorial(eval(e)))
    elif btn=="|x|":
        display_2.insert("end","|"+e+"|")
        if int(e)<0:
            ans.set(int(e)*-1)
        else:
            display.insert("end", btn)
    if btn in op:
                display_2.delete(0, tk.END)
                
#List of operators:
op=["+", "-", "*", "/" ]
#List of buttons
button_list = ["C", "AC", "√", "+", "π", "sin", "cos", "tan",
               "1", "2", "3", "-", "2π", "arcsin", "arccos","arctan",
               "4", "5", "6", "*", "|x|", "x^y", "1/x", "^2",
               "7", "8", "9", "/", "ln", "deg", "rad", "e",
               "0", "=", ".", "log10", "10^x", "(", ")", "x!"]
row_value = 2
column_value = 0

#creating buttons
for i in button_list:
    btn = tk.Button(window, text=i, width=7, height=2, bg='#313434', fg='white', font=('Times New Roman', 20),
                    command=lambda i=i: click(i))
    btn.grid(row=row_value, column=column_value)
    column_value += 1
    if column_value > 7:
        row_value += 1
        column_value = 0
window.mainloop()