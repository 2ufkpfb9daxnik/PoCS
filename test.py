from tkinter import *
root = Tk()

root.title('総合課題実習')
root.geometry('900x800')
root.resizable(False, False)

# Frame設定
frame1 = Frame(root, width=300, height=800, borderwidth=1, relief='solid')
frame2 = Frame(root, width=300, height=800, borderwidth=1, relief='solid')
frame3 = Frame(root, width=300, height=400, borderwidth=1, relief='solid')
frame4 = Frame(root, width=300, height=400, borderwidth=1, relief='solid')

# Frameサイズ固定
frame1.propagate(False)
frame2.propagate(False)
frame3.propagate(False)
frame4.propagate(False)

# Frame配置
frame1.grid(row=0, column=0, rowspan=2)
frame2.grid(row=0, column=1, rowspan=2)
frame3.grid(row=0, column=2)
frame4.grid(row=1, column=2)

# Widget配置
label = Label(frame2, text='label')
label.pack()
button = Button(frame1, text='Button')
button.pack()
entry = Entry(frame3)
entry.pack()
label = Label(frame4, text='おすすめ')
label.pack()

root.mainloop()