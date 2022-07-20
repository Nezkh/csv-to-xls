import pandas as pd

readfile = pd.read_csv("C:\\Users\\fcoma\\\Downloads\\csvtoxls\\tick.csv")

readfile.to_excel("C:\\Users\\fcoma\\\Downloads\\csvtoxls\\tick.xlsx", index=None, header=True)
