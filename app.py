import camelot
import numpy as np
import pandas as pd
from xpdf_python import to_text

tables = camelot.read_pdf("speiseplan_kw14_s1.pdf")
# print(tables)
tables.export('test.csv', f='csv', compress=True)
# print(tables[0])
# print(tables[0].parsing_report)
tables[0].to_csv('gerichte.csv')
# print(tables[0].df)
food_df = tables[0].df
print(food_df.iloc[1, 1])

tables = camelot.read_pdf("speiseplan_kw14_s2.pdf")
# print(tables)
tables.export('test.csv', f='csv', compress=True)
# print(tables[0])
# print(tables[0].parsing_report)
tables[0].to_csv('naehrwerte.csv')
# print(tables[0].df)
food_df = tables[0].df
print(food_df.iloc[1:6, 2])
