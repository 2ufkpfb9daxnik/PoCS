from tkinter import *
# import tkinter.ttk as ttk
from tkinter import ttk, font
from datetime import datetime
import csv
import webbrowser
import urllib.parse
root = Tk()

font50 = font.Font(size=50)
root.option_add("*Font", font50)

root.title('総合課題実習')
root.geometry('900x800')
root.resizable(False, False)

import datetime
thisyear = datetime.date.today().year

def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.

    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if
        elm[:2] != ('!disabled', '!selected')]

style = ttk.Style()
style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

def sortdisplay():
    date_list = []  # ループの外で date_list を初期化する
    
    with open("test.csv", "r", encoding="utf-8") as csv_file:
        global remaindate
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # date_str = f"{row[1]}/{row[2]}/{row[3]}"
            date_obj = datetime.date(int(row[1]), int(row[2]), int(row[3]))
            remaindate = date_obj - datetime.date.today()
            date_list.append((remaindate, row, date_obj))  # remaindate を最初に追加

    # remaindate を基準にして行をソート
    sorted_date_list = sorted(date_list, key=lambda x: x[0])
    children = table.get_children('')
    for child in children:
        table.delete(child)
    print(sorted_date_list)
    for remaindate, row, date_obj in sorted_date_list:
        values = (row[0], remaindate, date_obj)
        # table.insert(parent='', index='end', values=(values))

        item_id = table.insert(parent='', index='end', values=(values))

# remaindate が負の場合にタグを追加
        if remaindate < datetime.timedelta(days=1):
            table.item(item_id, tags=("negative_remaindate"))
        if datetime.timedelta(days=1) <remaindate < datetime.timedelta(days=6):
            table.item(item_id, tags=("underfive_remaindate"))


 
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
        global impyear, impmonth, impday, text, date
        impyear=yearset.get()
        impmonth=monthset.get()
        impday=dayset.get()
        # inputdate=datetime.date(int(impyear), int(impmonth), int(impday))
        date = f"{impyear}年{impmonth}月{impday}日"
        text = entry_2b.get() 
        data = [text, impyear,impmonth,impday]       #ここからファイル書き込み
        with open("test.csv", "a", newline="", encoding="utf-8") as csvfile:       
            writer = csv.writer(csvfile)
            writer.writerow(data)
        sortdisplay()

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

    setbutton=Button(window2_frame3, text='追加', font=('', 50), command=insert)
    setbutton.pack()

    def deletewindow():
        window2.destroy()

    deletewindow2=Button(window2_frame4, text='ウィンドウ削除', font=('', 50), command=deletewindow)
    deletewindow2.pack()
    window2.mainloop()

def delete_selected():
    selected_items = table.selection()  # 選択した行のIDを取得
    for selected_item in selected_items:
        # 選択したアイテムのIDを取得
        selected_id = table.item(selected_item, 'values')[0] if table.item(selected_item, 'values') else None

        # IDが存在するか確認
        if selected_id:
            # TreeViewから選択した行を削除
            table.delete(selected_item)

            # CSVファイルからも削除
            with open("test.csv", "r", encoding="utf-8") as csv_file:
                rows = list(csv.reader(csv_file))

            # 選択したIDの行を特定して削除
            rows = [row for row in rows if row[0] != selected_id]

            # CSVファイルを再書き込み
            with open("test.csv", "w", encoding="utf-8", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(rows)

# def convert_date_format(date_str):
#     # '2023-12-22' を 2023, 12, 22 に変換
    
#     date_obj = datetime.strptime(date_str, '%Y-%m-%d')
#     return date_obj.year, date_obj.month, date_obj.day

# def delete_selected():
#     selected_items = table.selection()  # 選択した行のIDを取得
#     for selected_item in selected_items:
#         # 選択したアイテムのvaluesを取得
#         selected_values = table.item(selected_item, 'values') if table.item(selected_item, 'values') else None

#         # valuesが存在するか確認
#         if selected_values:
#             # TreeViewから選択した行を削除
#             table.delete(selected_item)

#             # CSVファイルからも削除
#             with open("test.csv", "r", encoding="utf-8") as csv_file:
#                 rows = list(csv.reader(csv_file))

#             # 選択した行を特定して削除
#             rows = [row for row in rows if row[2] != convert_date_format(selected_values[2])]

#             # CSVファイルを再書き込み
#             with open("test.csv", "w", encoding="utf-8", newline='') as csv_file:
#                 csv_writer = csv.writer(csv_file)
#                 csv_writer.writerows(rows)

# 2023-12-22 を 2023, 12, 22 に変換する関数の呼び出し例
# convert_date_format('2023-12-22')



# Frame設定
frame1 = Frame(root, width=600, height=800, borderwidth=1, relief='solid', padx=10, pady=10)
frame2 = Frame(root, width=300, height=500, borderwidth=1, relief='solid', padx=10, pady=10)
frame3 = Frame(root, width=300, height=300, borderwidth=1, relief='solid', padx=10, pady=10)

# Frameサイズ固定
frame1.propagate(False)
frame2.propagate(False)
frame3.propagate(False)

# Frame配置
frame1.grid(row=0, column=0, rowspan=2)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=1)

# Widget配置
add = Button(frame2, text='追加', font=('', 50),command=button)
add.pack()
delete = Button(frame2, text='削除', font=('',50),command=delete_selected)
delete.pack()
update = Button(frame2, text='更新', font=('', 50), command=sortdisplay)
update.pack()

columns= ('name', 'remain','date')
table = ttk.Treeview(frame1, columns=columns, height=49, show="headings")
table.column('name', anchor=W, width=200, stretch='no')
table.column('date', anchor=W, width=200, stretch='no')
table.column('remain',anchor=W, width=200, stretch='no')
table.heading('name', text='食品名', anchor=NW)
table.heading('date', text='期限', anchor=NW)
table.heading('remain',text='残り時間', anchor=NW)
table.tag_configure("negative_remaindate", background="red")
table.tag_configure("underfive_remaindate", background="yellow")
table.pack()

def search_and_open_browser():
    selected_item_id = table.selection()

    if selected_item_id:
        selected_item_values = table.item(selected_item_id)['values']
        if selected_item_values:
            # 先頭の要素を取得
            first_element = selected_item_values[0]
            search_word = f"{first_element} レシピ"
    # 検索ワードをURLエンコードする
            encoded_search_word = urllib.parse.quote(search_word) 

    # Googleで検索するURLを構築する（他の検索エンジンを使用する場合はURLを変更）
            search_url = f"https://www.google.com/search?q={encoded_search_word}"

    # デフォルトのWebブラウザで検索結果を表示する
            webbrowser.open(search_url)

search = Button(frame2, text="検索", font=('', 50), command=search_and_open_browser)
search.pack()
# label = Label(frame3, text='最終更新:', font=('', 50))
# label.pack()

sortdisplay()

root.mainloop()