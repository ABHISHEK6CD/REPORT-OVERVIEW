import pandas as pd
from ydata_profiling import ProfileReport
df = pd.read_csv('HR_Analytics.csv')
profile = ProfileReport(df, title="HR Analytics Profile Report", explorative=True)
profile.to_file("index.html")
