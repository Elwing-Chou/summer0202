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
# 產生視窗
screen = pg.display.set_mode([width, height])
# 設定遊戲標題
pg.display.set_caption("象棋")
# 建立畫布bg
bg = pg.Surface(screen.get_size())
# 把畫布填滿某個顏色
bg.fill([199, 167, 82])
screen.blit(bg, [0, 0])
# 對畫面進行更新(才會真的秀出來)
pg.display.update()

running = True
while running:
    # 收取你的遊戲任何事件(滑鼠點擊/鍵盤按鈕...)
    for event in pg.event.get():
        # 偵測滑鼠點擊以後放掉的動作
        if event.type == pg.MOUSEBUTTONUP:
            pass
        # 如果收到的事件是按x
        if event.type == pg.QUIT:
            # 迴圈就會變成while False
            running = False

pg.quit()