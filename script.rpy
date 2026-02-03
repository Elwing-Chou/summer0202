
define usagi = Character("烏薩奇")
define e = Character("[player]")

label start:

    scene bg forest:
        xysize(1920, 1080)

    show usagi normal at center:
        xysize(1000, 1000)

    "來玩個遊戲吧"

label name:
    usagi "你叫什麼?"
    $ player = renpy.input("請輸入姓名")

    usagi "你是叫[player]嗎?"
    menu:
        "是":
            e "是的!"
        "否":
            jump name

default win = 0
default lose = 0
default even = 0

label game:
    menu:
        "剪刀":
            $ my = 0
        "石頭":
            $ my = 1
        "布":
            $ my = 2

    $ com = renpy.random.randint(0, 2)

    if com == 0:
        show usagi scissor at center:
            xysize(1000, 1000)
        usagi "剪刀!!!"
    elif com == 1:
        show usagi stone  at center:
            xysize(1000, 1000)
        usagi "石頭!!!"
    else:
        show usagi paper at center:
            xysize(1000, 1000)
        usagi "布!!!"

    if my == (com + 1) % 3:
        $ win = win + 1
    elif com == (my + 1) % 3:
        $ lose = lose + 1
    else:
        $ even = even + 1

    if win == 3:
        usagi "你贏了!!!"
    elif lose == 3:
        usagi "你輸了???"
    else:
        usagi "贏:[win] 輸:[lose] 平:[even]"
        jump game