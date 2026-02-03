# 遊戲腳本位於此檔案。

# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define usagi = Character("烏薩奇")
define e = Character("[player]")


# 遊戲從這裡開始。

label start:

    # 顯示背景。 預設情況下，它使用佔位符，但您可以
    # 將檔案（名為 "bg room.png" 或 "bg room.jpg"）新增至
    # images 目錄來顯示它。

    scene bg forest

    # 這顯示了一個角色精靈。 使用了佔位符，但您可以
    # 透過將名為 "eileen happy.png" 的檔案
    # 新增至 images 目錄來取代它。

    show usagi normal at center:
        xysize(1000, 1000)

    # 這些顯示對話行。
    "來玩個遊戲吧"

label name:
    usagi "你叫什麼?"
    $ player = renpy.input("請輸入姓名")
    # 遊戲結束。

    usagi "你是叫[player]嗎?"
    menu:
        "是":
            e "是的!"
        "否":
            jump name
    return
