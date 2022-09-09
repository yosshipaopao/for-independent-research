# -*- coding: utf-8 -*-
import asyncio  # 非同期実行用 # pip install asyncio
import winsound  # windows用音声ツール # pip install winsound
import tkinter as tk  # GUI表示ツール # pip install tkinter
import time  # 時間用モジュール 停止と測定の役割 # デフォルトなのでインストール必要なし
import random  # ランダムモジュール　停止時間のランダム化 # デフォルトなのでインストール必要なし
import requests  # web通信ツール  サーバーにデータを送信 #pip install requests

# 画面の表示
root = tk.Tk()
root.title(u"自由研究用のやつ")
root.geometry("1500x800")

# グローバル変数の指定(複数の関数で使用する)
global mode
global running
global time_start
global shapes
global data
data = {}
shapes = {}
running = False
mode = 0

# メインの関数 どのキーが押されても実行されます


def on_key(event):
    # グローバル変数の利用
    global shapes
    global mode
    global running
    global time_start
    # 押されたキーの所得
    key = event.keysym
    # 実行している途中かスペースキーでなかったら終了
    if running or key != "space":
        return 0
    # 何回目の実行化を検出
    mode += 1
    if mode == 1:
        running = True
        # 画面にある説明用文章を削除
        setumei.destroy()
        zokkou.destroy()
        root.update()
        # ランダムで数秒待つ
        time.sleep(random.uniform(1, 3))
        running = False
        # 画面全体に黒い四角形を表示
        shapes["1"] = can.create_rectangle(0, 0, 1500, 800, fill="black")
        # カウントの開始。アプリの実行時間を変数に代入少数14桁?
        time_start = time.perf_counter()
    if mode == 2:
        # カウントの終了。アプリの実行時間を変数に代入。差が反応までの時間となる
        time_end = time.perf_counter()
        print(time_end-time_start)
        # 画面に表示してあるオブジェクトの削除
        can.delete(shapes["1"])
        # 送信用データに代入
        data["full_black"] = time_end-time_start
        # 結果の表示と続行メッセージを表示
        shapes["2"] = {}
        shapes["2"]["str"] = can.create_text(
            700, 300, text=time_end-time_start, fill="black", font=("", 30))
        shapes["2"]["zok"] = can.create_text(
            700, 700, text='spaceキーで続行...', fill="black", font=("", 30))
    if mode == 3:
        can.delete(shapes["2"]["str"])
        can.delete(shapes["2"]["zok"])
        root.update()
        time.sleep(random.uniform(1, 3))
        shapes["3"] = can.create_rectangle(0, 0, 1500, 800, fill="red")
        time_start = time.perf_counter()
    if mode == 4:
        time_end = time.perf_counter()
        data["full_red"] = time_end-time_start
        can.delete(shapes["3"])
        shapes["4"] = {}
        shapes["4"]["time"] = can.create_text(
            700, 300, text=time_end-time_start, fill="black", font=("", 30))
        shapes["4"]["zok"] = can.create_text(
            700, 700, text='spaceキーで続行...', fill="black", font=("", 30))
        print(time_end-time_start)
    if mode == 5:
        can.delete(shapes["4"]["time"])
        can.delete(shapes["4"]["zok"])
        root.update()
        time.sleep(random.uniform(1, 3))
        shapes["16"] = can.create_rectangle(0, 0, 1500, 800, fill="#888")
        time_start = time.perf_counter()
    if mode == 6:
        time_end = time.perf_counter()
        data["full_hai"] = time_end-time_start
        can.delete(shapes["16"])
        shapes["17"] = {}
        shapes["17"]["time"] = can.create_text(
            700, 300, text=time_end-time_start, fill="black", font=("", 30))
        shapes["17"]["zok"] = can.create_text(
            700, 700, text='spaceキーで続行...', fill="black", font=("", 30))
        print(time_end-time_start)
    if mode == 7:
        can.delete(shapes["17"]["time"])
        can.delete(shapes["17"]["zok"])
        root.update()
        time.sleep(random.uniform(1, 3))
        shapes["5"] = can.create_rectangle(700, 350, 800, 450, fill="black")
        time_start = time.perf_counter()
    if mode == 8:
        time_end = time.perf_counter()
        data["min_black"] = time_end-time_start
        can.delete(shapes["5"])
        shapes["6"] = {}
        shapes["6"]["time"] = can.create_text(
            700, 300, text=time_end-time_start, fill="black", font=("", 30))
        shapes["6"]["zok"] = can.create_text(
            700, 700, text='spaceキーで続行...', fill="black", font=("", 30))
        print(time_end-time_start)
    if mode == 9:
        can.delete(shapes["6"]["time"])
        can.delete(shapes["6"]["zok"])
        root.update()
        time.sleep(random.uniform(1, 3))
        shapes["7"] = can.create_rectangle(700, 350, 800, 450, fill="red")
        time_start = time.perf_counter()
    if mode == 10:
        time_end = time.perf_counter()
        data["min_red"] = time_end-time_start
        can.delete(shapes["7"])
        shapes["8"] = {}
        shapes["8"]["time"] = can.create_text(
            700, 300, text=time_end-time_start, fill="black", font=("", 30))
        shapes["8"]["zok"] = can.create_text(
            700, 700, text='spaceキーで続行...', fill="black", font=("", 30))
        print(time_end-time_start)

    if mode == 11:
        can.delete(shapes["8"]["time"])
        can.delete(shapes["8"]["zok"])
        root.update()
        time.sleep(random.uniform(1, 3))
        shapes["18"] = can.create_rectangle(700, 350, 800, 450, fill="#888")
        time_start = time.perf_counter()
    if mode == 12:
        time_end = time.perf_counter()
        data["min_hai"] = time_end-time_start
        can.delete(shapes["18"])
        shapes["19"] = {}
        shapes["19"]["time"] = can.create_text(
            700, 300, text=time_end-time_start, fill="black", font=("", 30))
        shapes["19"]["zok"] = can.create_text(
            700, 700, text='spaceキーで続行...', fill="black", font=("", 30))
        print(time_end-time_start)
    if mode == 13:
        can.delete(shapes["19"]["time"])
        can.delete(shapes["19"]["zok"])
        root.update()
        time.sleep(random.uniform(1, 3))
        # 4000Hzで1000ミリ秒(1秒)音を流す
        asyncio.new_event_loop().run_in_executor(None, winsound.Beep, 4000, 1000)
        time_start = time.perf_counter()
    if mode == 14:
        time_end = time.perf_counter()
        data["son_h"] = time_end-time_start
        shapes["10"] = {}
        shapes["10"]["time"] = can.create_text(
            700, 300, text=time_end-time_start, fill="black", font=("", 30))
        shapes["10"]["zok"] = can.create_text(
            700, 700, text='spaceキーで続行...', fill="black", font=("", 30))
        print(time_end-time_start)
    if mode == 15:
        can.delete(shapes["10"]["time"])
        can.delete(shapes["10"]["zok"])
        root.update()
        time.sleep(random.uniform(1, 3))
        asyncio.new_event_loop().run_in_executor(None, winsound.Beep, 500, 1000)
        time_start = time.perf_counter()
    if mode == 16:
        time_end = time.perf_counter()
        data["son_l"] = time_end-time_start
        shapes["12"] = {}
        shapes["12"]["time"] = can.create_text(
            700, 300, text=time_end-time_start, fill="black", font=("", 30))
        shapes["12"]["zok"] = can.create_text(
            700, 700, text='spaceキーで続行...', fill="black", font=("", 30))
        print(time_end-time_start)
    if mode == 17:
        print(data)
        # サーバーにそうしんする準備
        params = data
        # 送信するURl
        url = 'https://test.yosshipaopao.com/jiyu.php'
        # 返されたデータ
        response = requests.get(url, params=params)
        print(response.text)
        can.delete(shapes["12"]["time"])
        can.delete(shapes["12"]["zok"])
        # 送信されて帰ってきたデータの表示
        can.create_text(700, 300, text=response.text,
                        fill="black", font=("", 30))


# aは入力されたキーボードの検出用オブジェクト
a = tk.Label(root, textvariable="")
a.pack()
# 押されたときに実行
a.bind('<Key>', on_key)  # ④
a.focus_set()  # ⑤
can = tk.Canvas(root, height=800, width=1500)
can.pack()
setumei = tk.Label(font=("", 40), text=u'画面に変更があるか音が出たときに\nすぐspace キーを押してください')
setumei.place(x=350, y=300)
zokkou = tk.Label(text=u'spaceキーで続行...')
zokkou.place(x=700, y=700)

# 画面の毎回更新
root.mainloop()
