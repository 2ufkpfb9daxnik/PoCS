from tkinter import *

def click_btn_2a():
    button_2a['text'] = 'クリックしました'

def selected():
    indices = lst_b.curselection()
    selections = '\n'.join([lst_b.get(i) for i in indices])
    sel_v.set(f'{selections}')

if __name__ == '__main__':

    root = Tk()  # この下に画面構成を記述

    # ----------- ①Window作成 ----------- #
    root.title('tkinterの使い方')   # 画面タイトル設定
    root.geometry('750x450')        # 画面サイズ設定
    root.resizable(False, False)    # リサイズ不可に設定

    # ----------- ②Frameを定義 ----------- #
    frame1 = Frame(root, width=250, height=150)  # Label
    frame2 = Frame(root, width=250, height=150)  # Button, Entry
    frame3 = Frame(root, width=250, height=150)  # CheckButton
    frame4 = Frame(root, width=250, height=150)  # RadioButton
    frame5 = Frame(root, width=250, height=150)  # Spinbox
    frame6 = Frame(root, width=250, height=150)  # Listbox
    frame7 = Frame(root, width=250, height=150)  # Canvas
    frame8 = Frame(root, width=250, height=150)  # Canvas用ボタン
    frame9 = Frame(root, width=250, height=150)  # Photoimage

    # Frameサイズを固定
    frame1.propagate(False)
    frame2.propagate(False)
    frame6.propagate(False)
    frame7.propagate(False)
    frame8.propagate(False)
    frame9.propagate(False)

    # Frameを配置(grid)
    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=1)
    frame3.grid(row=0, column=2)
    frame4.grid(row=1, column=0)
    frame5.grid(row=1, column=1)
    frame6.grid(row=1, column=2)
    frame7.grid(row=2, column=0)
    frame8.grid(row=2, column=1)
    frame9.grid(row=2, column=2)

    # ---------- ③Widget配置  ----------- #
    # == label(Frame1) == # 
    label_1a = Label(frame1, text='ラベルの文字列', font=('', 14), bg='#ccccff', fg='#ff0000')
    label_1b = Label(frame1, text='ラベル左寄せ', font=('System', 14))
    label_1a.pack(padx=5, pady=10)
    label_1b.pack(anchor=W)


    # == Button(Frame2) == # 
    button_2a = Button(frame2, text='ボタン名変更', command=click_btn_2a)
    button_2a.pack(padx=5, pady=10, expand=True)

    # == Entry(Frame2) == # 
    entry_2b = Entry(frame2, width=14)
    text = StringVar()
    button_2b = Button(frame2, text='文字列コピー',
                command=lambda: text.set(entry_2b.get()))
    label_2b = Label(frame2, textvariable=text, font=('System', 14))
    entry_2b.pack()
    button_2b.pack()
    label_2b.pack()


    # == Checkbutton(Frame3) == # 
    chk_v1 = StringVar()
    chk_v1.set('0') # 初期化
    chk_b1 = Checkbutton(frame3, text='オプション1', variable=chk_v1)
    chk_v2 = StringVar()
    chk_v2.set('２未選択') # 初期化
    chk_b2 = Checkbutton(frame3, text='オプション2', onvalue='２選択', offvalue='２未選択', variable=chk_v2)
    # 状態表示ボタン
    chk_value = StringVar()
    chk_value.set('')
    button_chk = Button(frame3, text='状態表示',
                command=lambda: chk_value.set('%s, %s' % (chk_v1.get(), chk_v2.get())))
    # 状態表示ラベル
    label_chk = Label(frame3, textvariable=chk_value, font=(10))
    chk_b1.grid(row=0, column=0)
    chk_b2.grid(row=0, column=1)
    button_chk.grid(row=1, column=0, columnspan=2, pady=5)
    label_chk.grid(row=2, pady=5, columnspan=2)


    # == Radiobutton(Frame4) == # 
    label_frame = LabelFrame(frame4, text='Options')
    rad_v1 = StringVar()
    rad_v1.set('0')
    rad_b1 = Radiobutton(label_frame, text='オプションA', value='A', variable=rad_v1)
    rad_b2 = Radiobutton(label_frame, text='オプションB', value='B', variable=rad_v1)
    rad_value = StringVar()
    rad_value.set('')
    button_rad = Button(frame4, text='選択', command=lambda : rad_value.set('%s' % rad_v1.get()))
    label_rad = Label(frame4, textvariable=rad_value, font=(10))
    label_frame.grid(row=0, column=0)
    rad_b1.grid(row=0, column=0)
    rad_b2.grid(row=0, column=1)
    button_rad.grid(row=1, pady=5)
    label_rad.grid(row=2)


    # == Spinbox(Frame5) == #
    spn_v = StringVar()
    spn_v.set('東京')
    cities = ['東京', '名古屋', '大阪']
    spn_value = StringVar()
    spn_value.set('東京')
    spin = Spinbox(frame5, state='readonly', textvariable=spn_v, values=cities, command=lambda: spn_value.set('%s' % spn_v.get()))
    label_spin = Label(frame5, textvariable=spn_value)
    spin.grid(row=0, column=0, pady=5)
    label_spin.grid(row=1, column=0)


    # == Listbox(Frame6) == #
    countries = ['日本', 'アメリカ', '中国']
    lst_v = StringVar(value=countries)
    lst_b = Listbox(frame6, listvariable=lst_v, selectmode='multiple', height=4)
    button_lst = Button(frame6, text='選択', command=selected)
    sel_v = StringVar()
    label_lst = Label(frame6, textvariable=sel_v)
    lst_b.pack(side='left', padx=5)
    button_lst.pack(side='left', padx=5)
    label_lst.pack(side='left', padx=5)


    # == Canvas(Frame7) == # 
    canvas = Canvas(frame7, width=250, height=200)
    canvas.create_rectangle(0, 0, 250, 200, fill='white')
    canvas.pack()


    # == Canvas操作用ボタン(Frame8) == # 
    button_8a = Button(frame8, text='描く', width=15,
                command=lambda: canvas.create_rectangle(10, 10, 140, 140, tag='rect'))
    button_8a.pack(padx=5, pady=10)
    button_8b = Button(frame8, text='削除', width=15,
                command=lambda: canvas.delete('rect'))
    button_8b.pack(padx=5, pady=10)


    # 画像表示 (Frame9) == # 
    #image = PhotoImage(file='./python_logo.png')
    #label_9 = Label(frame9, image=image)
    #label_9.pack(pady=20)

    root.mainloop()