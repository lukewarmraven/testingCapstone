from test3 import normalData
from pprint import pprint
import pandas as pd

from sklearn.cluster import KMeans
import folium

import matplotlib.pyplot as plt
import seaborn as sns


#pprint(normalData[0], sort_dicts=False)

normal = pd.DataFrame(normalData)

locNormal = normal[["lat","lng"]]

model = KMeans(n_clusters=3)
y_kmeans = model.fit_predict(locNormal)

normal['result'] = y_kmeans

#print(normal)
#normal.to_csv("normalClustered.csv",index=False)
#print(normal)
#plt.scatter(normal["lng"],normal["lat"],c=normal['result'])
#plt.show()

# trying to map them in google maps
import gmplot

api_key = "AIzaSyDi9vaie4KqH6Lu7RvZE9LPBLKg-Sm0CFU"
lat = data['lat'].tolist()
lng = data['lng'].tolist()
result = data['result'].tolist()

colors = ['red','blue','green']
clusterColor = [colors[cluster] for cluster in result]

gmap1 = gmplot.GoogleMapPlotter(14.660915632697726, 121.10051851107902,15,apikey=api_key)
#gmap1.scatter(lat,lng,'#ff0000',size=10,marker='o')

for latPoint,lngPoint, color in zip(lat,lng,clusterColor):
    gmap1.marker(latPoint,lngPoint,color=color)

gmap1.draw('map1.html')