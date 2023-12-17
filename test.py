from tkinter import *
# import tkinter.ttk as ttk
from tkinter import ttk, font
import datetime
import csv
root = Tk()

font50 = font.Font(size=50)
root.option_add("*Font", font50)

root.title('総合課題実習')
root.geometry('900x800')
root.resizable(False, False)

thisyear = datetime.date.today().year

def sortANDdisplay():
    with open("test.csv","r",encoding="ms932")as csv_file:
        reader = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    for row in range(1):
        table.insert(parent='', index='end', values=(row[1],row[2],row[3]))#ソフト上に表示

def button():
    window2=Toplevel(root)
    window2.focus()
    window2.geometry("550x400")
    window2.title("食品追加")

    window2_frame1=Frame(window2, width=550, height=100, relief='solid', padx=10, pady=10)
    window2_frame2=Frame(window2, width=550, height=100, relief='solid', padx=10, pady=10)
    window2_frame3=Frame(window2, width=550, height=100, relief='solid', padx=10, pady=10)
    window2_frame4=Frame(window2, width=550, height=100, relief='solid', padx=10, pady=10)

    window2_frame1.propagate(False)
    window2_frame2.propagate(False)
    window2_frame3.propagate(False)
    window2_frame4.propagate(False)

    window2_frame1.grid(row=0)
    window2_frame2.grid(row=1)
    window2_frame3.grid(row=2)
    window2_frame4.grid(row=3)

    entry_2b =Entry(window2_frame1, width=200, font=('', 50))
    #text = StringVar()
    entry_2b.pack()

    def insert():
        global impyear, impmonth, impday, remaindate, text, date
        impyear=yearset.get()
        impmonth=monthset.get()
        impday=dayset.get()
        inputdate=datetime.date(int(impyear), int(impmonth), int(impday))
        nowdate=datetime.date.today()
        remaindate =inputdate-nowdate
        date = f"{impyear}年{impmonth}月{impday}日"
        text = entry_2b.get() 
        data = [text, impyear,impmonth,impday]       #ここからファイル書き込み
        with open("test.csv", "a", newline="") as csvfile:        # CSVファイルを新規作成してデータを書き込む
            writer = csv.writer(csvfile)
            writer.writerow(data)
        sortANDdisplay()

    yearset=ttk.Combobox(window2_frame2, width=4, height=10, values=[str(i) for i in range(thisyear, thisyear+5)], font=('', 50))
    yearset.pack(side=LEFT)

    yearsetlabel=Label(window2_frame2, text='年', font=('', 50))
    yearsetlabel.pack(side=LEFT)

    monthset=ttk.Combobox(window2_frame2, width=2, height=12, values=[str(i) for i in range(1,13)], font=('', 50))
    monthset.pack(side=LEFT)

    monthsetlabel=Label(window2_frame2, text='月', font=('', 50))
    monthsetlabel.pack(side=LEFT)

    dayset=ttk.Combobox(window2_frame2, width=2, height=10, values=[str(i) for i in range(1,32)], font=('', 50))
    dayset.pack(side=LEFT)

    daysetlabel=Label(window2_frame2, text='日', font=('', 50))
    daysetlabel.pack(side=LEFT)

    setbutton=Button(window2_frame3, text='食品追加', font=('', 50), command=insert)
    setbutton.pack()

    def deletewindow():
        window2.destroy()

    deletewindow2=Button(window2_frame4, text='ウィンドウ削除', font=('', 50), command=deletewindow)
    deletewindow2.pack()
    window2.mainloop()

def delete_selected():
    selected_items = table.selection()  # 選択した行のIDを取得
    for selected_item in selected_items:
        table.delete(selected_item)  # 選択した行を削除





# Frame設定
frame1 = Frame(root, width=600, height=800, borderwidth=1, relief='solid', padx=10, pady=10)
frame2 = Frame(root, width=300, height=400, borderwidth=1, relief='solid', padx=10, pady=10)
frame3 = Frame(root, width=300, height=400, borderwidth=1, relief='solid', padx=10, pady=10)

# Frameサイズ固定
frame1.propagate(False)
frame2.propagate(False)
frame3.propagate(False)

# Frame配置
frame1.grid(row=0, column=0, rowspan=2)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=1)

# Widget配置
add = Button(frame2, text='食品追加', font=('', 50),command=button)
add.pack()
delete = Button(frame2, text='食品削除', font=('',50),command=delete_selected)
delete.pack()
update = Button(frame2, text='更新', font=('', 50), command=button)
update.pack()
label = Label(frame3, text='おすすめ', font=('', 50))
label.pack()

columns= ('name', 'remain','date')
table = ttk.Treeview(frame1, columns=columns, height=49, show="headings")
table.column('name', anchor=W, width=200, stretch='no')
table.column('date', anchor=W, width=200, stretch='no')
table.column('remain',anchor=W, width=200, stretch='no')
table.heading('name', text='食品名', anchor=NW)
table.heading('date', text='期限', anchor=NW)
table.heading('remain',text='残り時間', anchor=NW)
table.pack()




root.mainloop()