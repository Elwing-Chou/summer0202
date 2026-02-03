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
width, height = 800, 800
x_inter, y_inter = 80, 70
# 產生視窗
screen = pg.display.set_mode((width, height))
# 設定遊戲標題
pg.display.set_caption("象棋")

role = {
    0:["將", "帥"],
    1:["士", "仕"],
    2:["象", "相"],
    3:["馬", "傌"],
    4:["車", "俥"],
    5:["包", "炮"],
    6:["卒", "兵"],
}
board_cor = [[(0, 0)] * 9 for i in range(10)]
for i in range(9):
    for j in range(5):
        x, y = x_inter + i * x_inter, y_inter + j * y_inter
        board_cor[j][i] = (x, y)
for i in range(9):
    for j in range(5):
        x, y = x_inter + i * x_inter, 6 * y_inter + j * y_inter
        board_cor[j+5][i] = (x, y)


board_role = [[-1] * 9 for i in range(10)]
board_role[0][4] = (0, 0)
board_role[9][4] = (0, 1)

board_role[0][3] = (1, 0)
board_role[9][3] = (1, 1)
board_role[0][5] = (1, 0)
board_role[9][5] = (1, 1)

board_role[0][2] = (2, 0)
board_role[9][2] = (2, 1)
board_role[0][6] = (2, 0)
board_role[9][6] = (2, 1)

board_role[0][1] = (3, 0)
board_role[9][1] = (3, 1)
board_role[0][7] = (3, 0)
board_role[9][7] = (3, 1)

board_role[0][0] = (4, 0)
board_role[9][0] = (4, 1)
board_role[0][8] = (4, 0)
board_role[9][8] = (4, 1)

board_role[2][1] = (5, 0)
board_role[2][7] = (5, 0)
board_role[7][1] = (5, 1)
board_role[7][7] = (5, 1)

for i in range(5):
    board_role[3][2*i] = (6, 0)
    board_role[6][2*i] = (6, 1)

def refresh():
    # 建立畫布bg
    bg = pg.Surface(screen.get_size())
    # 把畫布填滿某個顏色
    bg.fill((199, 167, 82))

    # 把棋盤的直線畫出來(直線與直線間隔40)
    # pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)
    # 棋盤跟最左最右空隙45
    for i in range(10):
        x_start, y_start = x_inter, y_inter + i * y_inter
        x_end, y_end = x_inter + 8 * x_inter, y_inter + i * y_inter
        pg.draw.line(bg, (50, 50, 50), (x_start, y_start), (x_end, y_end), 2)

    for i in range(9):
        x_start, y_start = x_inter + i * x_inter, y_inter
        x_end, y_end = x_inter + i * x_inter, y_inter + 4 * y_inter
        pg.draw.line(bg, (50, 50, 50), (x_start, y_start), (x_end, y_end), 2)

        x_start, y_start = x_inter + i * x_inter, y_inter + 5 * y_inter
        x_end, y_end = x_inter + i * x_inter, y_inter + 9 * y_inter
        pg.draw.line(bg, (50, 50, 50), (x_start, y_start), (x_end, y_end), 2)

    x_start, y_start = x_inter + 3 * x_inter, y_inter
    x_end, y_end = x_inter + 5 * x_inter, y_inter + 2 * y_inter
    pg.draw.line(bg, (50, 50, 50), (x_start, y_start), (x_end, y_end), 2)

    x_start, y_start = x_inter + 5 * x_inter, y_inter
    x_end, y_end = x_inter + 3 * x_inter, y_inter + 2 * y_inter
    pg.draw.line(bg, (50, 50, 50), (x_start, y_start), (x_end, y_end), 2)

    x_start, y_start = x_inter + 3 * x_inter, y_inter + 7 * y_inter
    x_end, y_end = x_inter + 5 * x_inter, y_inter + 9 * y_inter
    pg.draw.line(bg, (50, 50, 50), (x_start, y_start), (x_end, y_end), 2)

    x_start, y_start = x_inter + 3 * x_inter, y_inter + 9 * y_inter
    x_end, y_end = x_inter + 5 * x_inter, y_inter + 7 * y_inter
    pg.draw.line(bg, (50, 50, 50), (x_start, y_start), (x_end, y_end), 2)


    for i in range(10):
        for j in range(9):
            if not board_role[i][j] == -1:
                if board_role[i][j][1] == 0:
                    color = (0, 0, 0)
                    fcolor = (255, 255, 255)
                else:
                    color = (255, 255, 255)
                    fcolor = (0, 0, 0)
                pg.draw.circle(bg, color, board_cor[i][j], 30)
                r, s = board_role[i][j]
                txt = FONT_UI.render(role[r][s], True, fcolor)
                bg.blit(txt, txt.get_rect(center=board_cor[i][j]))

    screen.blit(bg, (0,0))
    # 對畫面進行更新(才會真的秀出來)
    pg.display.update()
    return bg

refresh()
# 建立一個永不結束的迴圈(遊戲才不會結束)
# 第幾回合
game_round = 0
chosen = None
running = True
while running:
    # 收取你的遊戲任何事件(滑鼠點擊/鍵盤按鈕...)
    for event in pg.event.get():
        # 偵測滑鼠點擊以後放掉的動作
        if event.type == pg.MOUSEBUTTONUP:
            bg = refresh()
            m_x, m_y = pg.mouse.get_pos()
            mind, mini, minj = float("inf"), -1, -1
            for i in range(10):
                for j in range(9):
                    x, y = board_cor[i][j]
                    d = abs(x - m_x) + abs(y - m_y)
                    if d < mind:
                        mind, mini, minj = d, i, j
            if chosen == None:
                if not board_role[mini][minj] == -1:
                    x, y = board_cor[mini][minj]
                    pg.draw.rect(bg, (0, 100, 0), (x-30, y-30, 60, 60), 2)
                    screen.blit(bg, (0, 0))
                    # 對畫面進行更新(才會真的秀出來)
                    pg.display.update()
                    chosen = (mini, minj)
            else:
                lasti, lastj = chosen
                board_role[mini][minj] = board_role[lasti][lastj]
                board_role[lasti][lastj] = -1
                refresh()
                chosen = None

        # 如果收到的事件是按x
        if event.type == pg.QUIT:
            # 迴圈就會變成while False
            running = False

pg.quit()