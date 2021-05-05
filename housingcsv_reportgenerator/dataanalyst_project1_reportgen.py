import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv("housing.csv")
profile=ProfileReport(df)
profile.to_file(output_file="vamsi3may.html")
