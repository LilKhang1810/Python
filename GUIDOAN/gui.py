from tkinter import *
from tkinter import messagebox
from database import *
def add():
    line=name.get()+ '-' + deadline.get() + '-' + satisfy.get()
    save(line)
    show()
def show():
    sv=read()
    listbox.delete(0,END)
    for i in sv:
        listbox.insert(END,i)

def sapxepLich():
    sv = read()
    for i in range(len(sv)):
        for j in range(len(sv)):
            x,y = sv[i],sv[j]
            if x[2]>y[2]:
                sv[i],sv[j] = y,x
    listbox.delete(0,END)
    for i in sv :
        listbox.insert(END,i)
def xoa():
    sv = read()
    listbox.delete(0,END)
root = Tk()

def exit_application():
    result = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát ứng dụng?")
    if result:
        root.quit()

name = StringVar()
deadline = StringVar()
satisfy = StringVar()

root.title('Quản lí task và deadline')
root.minsize(width=500,height=500)
Label(root,text='ỨNG DỤNG QUẢN LÍ TASK',fg='red',font=('Times New Roman',26,'bold'),width=25).grid(row=0)
listbox = Listbox(root,width=80,height=20)
listbox.grid(row=1,columnspan=2)
show()

Label(root,text='Tên task:',font=('Times New Roman',16,'bold')).grid(row=2,column=0)
Entry(root,width=40,textvariable=name).grid(row=2,column=1)

Label(root,text='Hạn chót:',font=('Times New Roman',16,'bold')).grid(row=3,column=0)
Entry(root,width=40,textvariable=deadline).grid(row=3,column=1)

Label(root,text='Độ thoả mãn:',font=('Times New Roman',16,'bold')).grid(row=4,column=0)
Entry(root,width=40,textvariable=satisfy).grid(row=4,column=1)

button = Frame(root)
Button(button,text='Thêm',command=add).pack(side=LEFT)
Button(button,text='Xoá',command=xoa).pack(side=LEFT)
Button(button,text='Sắp xếp',command=sapxepLich).pack(side=LEFT)
Button(button,text='Thoát',command=exit_application).pack(side=LEFT)
button.grid(row=5,column=1,columnspan=2)
root.mainloop()