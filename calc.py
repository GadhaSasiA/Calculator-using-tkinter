import tkinter as tk
root=tk.Tk()
root.title("Calculator")
root.geometry("550x600")
root.configure(bg='lightblue')

equation=""
def show(value):
    global equation
    equation+=value
    label2.config(text=equation)
def clear():
    global equation
    equation=""
    label2.config(text=equation)
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label2.config(text=result)
   

label1=tk.Label(root,text="Calculator",font=('Arial',30),fg='blue',bg='lightgray')
label2=tk.Label(root,width=15,height=1,text="",font=("arial",35))
label1.pack()
label2.pack()
button=tk.Button(root,text='c',width=3,height='-2',font=("Arial",30,"bold"),fg='blue',bg='red',command=lambda:clear()).place(x=65,y=130)
button=tk.Button(root,text='%',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("%")).place(x=170,y=130)
button=tk.Button(root,text='off',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',).place(x=280,y=130)
button=tk.Button(root,text='/',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("/")).place(x=390,y=130)

button=tk.Button(root,text='9',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("9")).place(x=65,y=230)
button=tk.Button(root,text='6',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("6")).place(x=65,y=330)
button=tk.Button(root,text='3',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("3")).place(x=65,y=430)
button=tk.Button(root,text='.',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show(".")).place(x=65,y=530)


button=tk.Button(root,text='8',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("8")).place(x=170,y=230)
button=tk.Button(root,text='5',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("5")).place(x=170,y=330)
button=tk.Button(root,text='2',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("2")).place(x=170,y=430)
button=tk.Button(root,text='0',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("0")).place(x=170,y=530)


button=tk.Button(root,text='7',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("7")).place(x=280,y=230)
button=tk.Button(root,text='4',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("4")).place(x=280,y=330)
button=tk.Button(root,text='1',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("1")).place(x=280,y=430)
button=tk.Button(root,text='+/-',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("+/-")).place(x=280,y=530)

button=tk.Button(root,text='*',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("*")).place(x=390,y=230)
button=tk.Button(root,text='-',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("-")).place(x=390,y=330)
button=tk.Button(root,text='+',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:show("+")).place(x=390,y=430)
button=tk.Button(root,text='=',width=3,height='1',font=("Arial",30,"bold"),fg='blue',bg='black',command=lambda:calculate()).place(x=390,y=530)
root.mainloop()


