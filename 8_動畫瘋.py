import urllib.request as req
import json
import os
import pandas as pd

name = "baha/吉伊卡哇"
# 如果資料夾不存在, make起來
if not os.path.exists(name):
    os.makedirs(name)

url = "https://api.gamer.com.tw/anime/v1/danmu.php?videoSn=36632&geo=TW%2CHK"
resp = req.urlopen(url)
resp_l = json.load(resp)
danmu = resp_l["data"]["danmu"]

sn = url.split("?")[1].split("&")[0].split("=")[1]
# CSV(comma-separated values)
# 姓名,身高
# Elwing,175
# DataFrame: pandas表格
df = pd.DataFrame(danmu)
fp = name + "/" + sn + ".csv"
df.to_csv(fp)
# df.to_excel("chiikawa.xlsx")