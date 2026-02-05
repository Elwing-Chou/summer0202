import urllib.request as req
import json
import pandas as pd

url = "https://api.gamer.com.tw/anime/v1/danmu.php?videoSn=36632&geo=TW%2CHK"
resp = req.urlopen(url)
resp_l = json.load(resp)
danmu = resp_l["data"]["danmu"]

# CSV(comma-separated values)
# 姓名,身高
# Elwing,175
# DataFrame: pandas表格
df = pd.DataFrame(danmu)
df.to_csv("chiikawa.csv")
df.to_excel("chiikawa.xlsx")