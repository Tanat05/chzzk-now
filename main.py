import httpx
import tkinter
from tkinter import *

channel_id = '8a13b48bf962d6266f646e584a4ee466' #스트리머 id
naver_api_url = f'https://api.chzzk.naver.com/service/v2/channels/{channel_id}/live-detail'
viewer = 0


def update():
    global viewer
    response = httpx.get(naver_api_url)
    if response.status_code == 200:
        data = response.json()
        title = data['content']['liveTitle']
        count_viewer = data['content']['concurrentUserCount']
        tag = data['content']['liveCategoryValue']
        thumbnail = data['content']['liveImageUrl'].replace('{type}', '1920')
        date = data['content']['openDate']
        adult = data['content']['adult']

        label = tkinter.Label(win, text=title, font=("", 14))
        label.place(x=0, y=0, width=500, height=200)

        label = tkinter.Label(win, text="제목", font=("", 25))
        label.place(x=0, y=10, width=500, height=40)

        label = tkinter.Label(win, text=tag.upper(), font=("", 15))
        label.place(x=0, y=201, width=250, height=199)

        label = tkinter.Label(win, text="주제", font=("", 25))
        label.place(x=0, y=211, width=250, height=39)

        label = tkinter.Label(win, text=count_viewer, font=("", 60))
        label.place(x=501, y=0, width=249, height=200)

        label = tkinter.Label(win, text="시청자 수", font=("", 25))
        label.place(x=501, y=10, width=249, height=40)

        label = tkinter.Label(win, text=count_viewer-viewer, font=("", 60))
        label.place(x=751, y=0, width=249, height=200)

        label = tkinter.Label(win, text="시청자 수 변동", font=("", 25))
        label.place(x=751, y=10, width=249, height=40)

        if adult == True:
            label = tkinter.Label(win, text="18+", font=("", 15))
            label.place(x=501, y=201, width=249, height=200)
        else:
            label = tkinter.Label(win, text="전체이용가", font=("", 15))
            label.place(x=501, y=201, width=249, height=200)

        label = tkinter.Label(win, text="청소년시청제한", font=("", 25))
        label.place(x=501, y=211, width=249, height=39)

        label = tkinter.Label(win, text=date, font=("", 15))
        label.place(x=751, y=201, width=249, height=199)

        label = tkinter.Label(win, text="업타임", font=("", 25))
        label.place(x=751, y=211, width=249, height=39)

        viewer = count_viewer
    else:
        print("오프라인")

    win.after(30000, update)
    
win = Tk()
win.title("치지직 status")
win.geometry('1000x400')
canvas = Canvas(win, width=1000, height=400)
canvas.pack()

canvas.create_line(0, 200, 1000, 200)
canvas.create_line(500, 0, 500, 400)
canvas.create_line(750, 0, 750, 400)
canvas.create_line(250, 200, 250, 400)

win.after(3000, update)

win.mainloop()
