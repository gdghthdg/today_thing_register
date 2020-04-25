
import tkinter as tk

root=tk.Tk() #生成root主窗口

label=tk.Label(root,text='Hello,GUI') #生成标签
label.pack()        #将标签添加到主窗口
button1=tk.Button(root,text='Button1') #生成button1
button1.pack(side=tk.LEFT)         #将button1添加到root主窗口
button2=tk.Button(root,text='Button2')
button2.pack(side=tk.RIGHT)
root.mainloop()             #进入消息循环（必需组件）