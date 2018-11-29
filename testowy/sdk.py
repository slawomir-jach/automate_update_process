import pandas as pd

calls_df = pd.read_html("https://developer.android.com/studio/" , header=0 , parse_dates=["Platform"]) 
var1 = calls_df[1]
print(var1)
