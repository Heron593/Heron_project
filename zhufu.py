import tkinter as tk
import random
import threading
import time
def dow():
    window = tk.Tk()
    width=window.winfo_screenwidth()
    height=window.winfo_screenheight()
    a=random.randrange(0,width)
    b=random.randrange(0,height)
    window.title('生日快乐')
    window.geometry("200x80"+"+"+str(a)+"+"+str(b))
    tk.Label(window,
        text='生日快乐！',    # 标签的文字
        bg='pink',     # 背景颜色
        font=('幼圆', 17),     # 字体和字体大小
        width=16, height=4  # 标签长宽
        ).pack()    # 固定窗口位置
    window.mainloop()
 
threads = []
for i in range(85):#需要的弹框数量
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()