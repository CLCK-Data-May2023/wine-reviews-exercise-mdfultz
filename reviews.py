import pandas as pd
import numpy as np

winereview = pd.read_csv("data/winemag-data-130k-v2.csv.zip", index_col=0)

count = winereview.country.value_counts()

points_avg = winereview.groupby('country')['points'].mean().round(1)

df = pd.DataFrame.merge(count, points_avg, on = 'country')

print(df)

df.to_csv('data/reviews-per-country.csv')