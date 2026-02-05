import pygame as pg

#pygame初始化
pg.init()

# --- 字型 ---
def get_font(size):
    for f in ['microsoftjhenghei', 'simhei', 'stheitirelight']:
        if f in pg.font.get_fonts():
            return pg.font.SysFont(f, size)
    return pg.font.SysFont(None, size)

FONT_UI = get_font(32)
#設定視窗
width, height = 800, 880
dif = 80

# 現在被選擇的棋子(None: 無)([i, j])
chosen = [0, 0]
# 準備我棋盤上每個位置對應的座標
board_coord = [[-1] * 9 for i in range(10)]
for i in range(10):
    for j in range(9):
        x = j * dif + dif
        y = i * dif + dif
        board_coord[i][j] = [x, y]

# 準備我棋盤上每個位置的角色
board_role = [[-1] * 9 for i in range(10)]
role = [
    ["將", "帥"],
    ["士", "仕"],
    ["象", "相"],
    ["馬", "傌"],
    ["車", "俥"],
    ["包", "炮"],
    ["卒", "兵"]
]
# [腳色(0-6), 陣營(0or1)]
# 將/帥
board_role[0][4] = [0, 0]
board_role[9][4] = [0, 1]

board_role[0][3] = [1, 0]
board_role[0][5] = [1, 0]
board_role[9][3] = [1, 1]
board_role[9][5] = [1, 1]

board_role[0][2] = [2, 0]
board_role[0][6] = [2, 0]
board_role[9][2] = [2, 1]
board_role[9][6] = [2, 1]

board_role[0][1] = [3, 0]
board_role[0][7] = [3, 0]
board_role[9][1] = [3, 1]
board_role[9][7] = [3, 1]

board_role[0][0] = [4, 0]
board_role[0][8] = [4, 0]
board_role[9][0] = [4, 1]
board_role[9][8] = [4, 1]

board_role[2][1] = [5, 0]
board_role[2][7] = [5, 0]
board_role[7][1] = [5, 1]
board_role[7][7] = [5, 1]

for i in range(5):
    board_role[3][2*i] = [6, 0]
    board_role[6][2*i] = [6, 1]

# 產生視窗
screen = pg.display.set_mode([width, height])
# 設定遊戲標題
pg.display.set_caption("象棋")

def draw_board():
    # 建立畫布bg
    bg = pg.Surface(screen.get_size())
    # 把畫布填滿某個顏色
    bg.fill([199, 167, 82])
    # 1. 線
    for i in range(10):
        pg.draw.line(bg, [0, 0 ,0], [dif, i*dif+dif], [width-dif, i*dif+dif], 2)

    for i in range(9):
        pg.draw.line(bg, [0, 0, 0], [i*dif+dif, dif], [i*dif+dif, 5*dif], 2)

    for i in range(9):
        pg.draw.line(bg, [0, 0, 0], [i*dif+dif, 6*dif], [i*dif+dif, 10*dif], 2)

    pg.draw.line(bg, [0, 0, 0], [4*dif, 1*dif], [6*dif, 3*dif], 2)
    pg.draw.line(bg, [0, 0, 0], [6*dif, 1*dif], [4*dif, 3*dif], 2)
    pg.draw.line(bg, [0, 0, 0], [4*dif, 8*dif], [6*dif, 10*dif], 2)
    pg.draw.line(bg, [0, 0, 0], [6*dif, 8*dif], [4*dif, 10*dif], 2)

    # 畫棋子
    # 走過棋盤
    for i in range(10):
        for j in range(9):
            # 不等於-1: 代表我剛剛有設定角色
            if not board_role[i][j] == -1:
                # 腳色, 陣營
                r, side = board_role[i][j]
                x, y = board_coord[i][j]
                # 不同陣營, 設定不同顏色
                if side == 0:
                    c = [0, 0, 0]
                    fc = [255, 255, 255]
                else:
                    c = [255, 255, 255]
                    fc = [0, 0, 0]
                # 背景/顏色/圓心/半徑
                pg.draw.circle(bg, c, [x, y],35)
                # 準備填上去的字
                t = FONT_UI.render(role[r][side], 1, fc)
                # 背景(bg)上面疊上t
                bg.blit(t, t.get_rect(center=[x, y]))

    # 劃出選取框(背景 顏色 [左上x 左上y 寬度 高度] 畫筆粗細)
    if not chosen == None:
        i, j = chosen
        cx, cy = board_coord[i][j]
        pg.draw.rect(bg, [0, 255, 0], [cx-35, cy-35, 70, 70], 2)

    screen.blit(bg, [0, 0])
    # 對畫面進行更新(才會真的秀出來)
    pg.display.update()

# 第一次繪製
draw_board()
running = True
while running:
    # 收取你的遊戲任何事件(滑鼠點擊/鍵盤按鈕...)
    for event in pg.event.get():
        # 偵測滑鼠點擊以後放掉的動作
        if event.type == pg.MOUSEBUTTONUP:
            # 找最小距離: 把點的位置和我們儲存的棋盤每一個座標算距離
            # 只要比上次距離小 我就記錄起來
            x, y = pg.mouse.get_pos()
            mind, minpos = float("inf"), -1
            for i in range(10):
                for j in range(9):
                    cx, cy = board_coord[i][j]
                    d = abs(x-cx) + abs(y-cy)
                    if d < mind:
                        mind, minpos = d, [i, j]
            # 如果你算出的位置有棋子, 就要有選取框
            mini, minj = minpos
            if not board_role[mini][minj] == -1:
                chosen = minpos
            # 如果沒棋子 把選取弄掉
            else:
                chosen = None
            draw_board()
        # 如果收到的事件是按x
        if event.type == pg.QUIT:
            # 迴圈就會變成while False
            running = False

pg.quit()