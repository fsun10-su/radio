
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from music import music_main
import os
from threading import Thread
import try2

a = ''
b = ''
c = ''


def main():
    def selectPath():
        path_ = askdirectory()  # 使用askdirectory()方法返回文件夹的路径
        if path_ == "":
            path.get()  # 当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
        else:
            # print(path_)
            # path_ = path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
            path.set(path_)
            content = path_file()
            file_inner.insert(END, content)


    def selectPath1():
        path1_ = askdirectory()  # 使用askdirectory()方法返回文件夹的路径
        if path1_ == "":
            path1.get()  # 当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
        else:
            # path1_ = path1_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
            path1.set(path1_)

    def openPath():
        filepath1 = v1.get()
        global a, b, c
        a = path.get()
        b = path1.get()
        c = filepath1
        messagebox.showinfo("消息", "设置完成！")
        root.destroy()

    def path_file():
        str = ''
        file_path = path.get()
        file_list = os.listdir(file_path)
        for i in range(len(file_list)):
            # if i % 2 != 0:
            #    str += file_list[i] + '    '
            # else:
            str += file_list[i] + '\n'
        return str

    root = Tk()
    root.title("排歌系统 1.0")
    path = StringVar()
    path1 = StringVar()
    v1 = StringVar()
    order1 = StringVar()
    order2 = StringVar()
    order3 = StringVar()
    order4 = StringVar()
    order5 = StringVar()

    # path.set(os.path.abspath("."))
    # path1.set(os.path.abspath("."))

    Label(root, text="目标路径:").grid(row=0, column=0)
    Entry(root, textvariable=path, state="readonly").grid(row=0, column=1, ipadx=100)
    Label(root, text="结果路径:").grid(row=1, column=0)
    Entry(root, textvariable=path1, state="readonly").grid(row=1, column=1, ipadx=100)
    Label(root, text="路径文件:").grid(row=6, column=0)

    Label(root, text="歌单文件夹名称:").grid(row=3, column=0)
    Entry(root, textvariable=v1).grid(row=3, column=1, padx=10, pady=5)

    Label(root, text="排单顺序:").grid(row=4, column=0,padx=5)
    Entry(root, textvariable=order1,width=5).place(x=200,y=92)
    Entry(root, textvariable=order2,width=5).place(x=280,y=92)
    Entry(root, textvariable=order3,width=5).place(x=360,y=92)
    Entry(root, textvariable=order4,width=5).place(x=440,y=92)
    Entry(root, textvariable=order5,width=5).place(x=520,y=92)

    file_inner = Text(root, height=5)
    file_inner.grid(row=6, column=1)


    Button(root, text="排歌歌单路径", command=selectPath).grid(row=0, column=2)
    Button(root, text="新建歌单位置", command=selectPath1).grid(row=1, column=2)
    # file_path = Button(root, text="提交", command=openPath).grid(row=3, column=1)
    Button(root, text="提交", command=openPath).grid(row=5, column=1,pady=15)
    root.mainloop()
    # print(a+'\n'+b+'\n'+c+'\n')
    # return (a+', '+b+', '+c)
    order1 = order1.get()
    order2 = order2.get()
    order3 = order3.get()
    order4 = order4.get()
    order5 = order5.get()
    order_list = [order1, order2, order3, order4, order5]
    for i in order_list:
        if i == '':
            order_list.remove(i)
    return a, b, c, order_list



if __name__ == '__main__':
    # print(main())
    origan, new_path, file_name, order_list = main()
    music_main(origan,new_path,file_name,order_list)