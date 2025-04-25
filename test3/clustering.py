from test3 import normalData
from pprint import pprint
import pandas as pd

from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

#pprint(normalData[0], sort_dicts=False)

normal = pd.DataFrame(normalData)

locNormal = normal[["lat","lng"]]

model = KMeans(n_clusters=10)
y_kmeans = model.fit_predict(locNormal)

normal['result'] = y_kmeans

#print(normal)
# save file to csv for mapPlotting
normal.to_csv("normalClustered.csv",index=False)
# check plotting here
plt.scatter(normal["lng"],normal["lat"],c=normal['result'])
plt.show()
