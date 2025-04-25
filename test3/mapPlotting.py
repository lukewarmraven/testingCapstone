import pandas as pd
import gmplot
#from clustering import normal
# my goal is to not import from the clustering file and instead access the csv produced from there

data = pd.read_csv('normalClustered.csv')

# trying to map them in google maps
import gmplot

api_key = "AIzaSyDi9vaie4KqH6Lu7RvZE9LPBLKg-Sm0CFU"
lat = data['lat'].tolist()
lng = data['lng'].tolist()
result = data['result'].tolist()

# add colors if u add another cluster
colors = ['red','blue','green','violet','yellow','orange','pink','white','black','brown']
clusterColor = [colors[cluster] for cluster in result]

gmap1 = gmplot.GoogleMapPlotter(14.660915632697726, 121.10051851107902,15,apikey=api_key)
#gmap1.scatter(lat,lng,'#ff0000',size=10,marker='o')

for latPoint,lngPoint, color in zip(lat,lng,clusterColor):
    gmap1.marker(latPoint,lngPoint,color=color)

gmap1.draw('newMap1.html')