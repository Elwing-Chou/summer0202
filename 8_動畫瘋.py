import urllib.request as req
import json
import os
import pandas as pd
import bs4 as bs

url = "https://ani.gamer.com.tw/animeVideo.php?sn=36632"
h = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",

}
r = req.Request(url, headers=h)
resp = req.urlopen(r)
html = bs.BeautifulSoup(resp)
for a in html.find_all("a"):
    href = a["href"]
    if href.startswith("?sn"):
        fullurl = "https://ani.gamer.com.tw/animeVideo.php" + href
        # print(fullurl)
        serial = href.split("=")[1]
        # 拿第幾集
        chapter = a.text
        print(chapter)

        # 下載一集的danmu
        name = "baha/吉伊卡哇"
        # 如果資料夾不存在, make起來
        if not os.path.exists(name):
            os.makedirs(name)

        url = "https://api.gamer.com.tw/anime/v1/danmu.php?videoSn=" + serial + "&geo=TW%2CHK"
        resp = req.urlopen(url)
        resp_l = json.load(resp)
        danmu = resp_l["data"]["danmu"]

        sn = url.split("?")[1].split("&")[0].split("=")[1]
        # CSV(comma-separated values)
        # 姓名,身高
        # Elwing,175
        # DataFrame: pandas表格
        df = pd.DataFrame(danmu)
        df["chapter"] = chapter
        fp = name + "/" + sn + ".csv"
        df.to_csv(fp)
        # df.to_excel("chiikawa.xlsx")