import os
import glob
import pandas as pd

name = "analyse"
if not os.path.exists(name):
    os.makedirs(name)

total = []
for fp in glob.glob("baha/*/*.csv"):
    df = pd.read_csv(fp, index_col=0)
    total.append(df)

total_df = pd.concat(total)
# print(total_df)
# step1找出到底有多少不同的留言id
uid = total_df["userid"].unique()
# step2走過這些id 進行篩選
for u in uid:
    print(u)
    # 比較每一格是否等於這id, 帶入表格篩選(True留下)
    result = total_df[total_df["userid"] == u]
    fp = name + "/" + u + ".csv"
    result.to_csv(fp)