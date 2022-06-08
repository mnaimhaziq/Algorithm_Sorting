import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gmplot

df = pd.read_csv("C:\\Users\\mnaim\\OneDrive\\Desktop\\Coding VSCO\\ADA\\ada project\\starbucks.csv", usecols=[
                 "latitude", "longitude"])
df.head()
df.plot(x="longitude", y="latitude", kind="scatter", colormap="YlOrRd")


# for x in range(len(df)):
#     gmap1 = gmplot.GoogleMapPlotter(df.iloc[x, 15],	df.iloc[x, 16],16)

#     gmap1.scatter(df.iloc[x, 15],	df.iloc[x, 16], '# FF0000',
#                   size=40, marker=False)
#     gmap1.polygon(df.iloc[x, 15],	df.iloc[x, 16],
#                   color='cornflowerblue')
#     gmap1.draw(
#         "C:\\Users\\mnaim\\OneDrive\\Desktop\\Coding VSCO\\ADA\\ada project\\map.html")
