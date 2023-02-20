"""The Pandas module deals with data: reading, analyzing, cleaning, etc"""
import pandas as pd

df = pd.read_csv("data.csv")

print(df.info())
