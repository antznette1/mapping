import folium
import pandas
data= pandas.read_csv("cities.csv")
lat= list(data["Latitude"])
lon= list(data["Longitude"])
place= list(data["Place Name"])

#creating markers for cities in westmidlands
def color_producer(place):
    if "West Midlands" in place:
        return "green"
    else:
        return "blue"
map = folium.Map(location=[52.591370,-2.110748],zoom_start=6, tiles ="Stamen Terrain")

#creating feature group for citites
fgp = folium.FeatureGroup(name= "Place")

#creating markers for cities in England

for lt,ln,pl in zip(lat,lon,place):
    fgp.add_child(folium.Marker(location = [lt,ln], popup=str(pl), icon = folium.Icon(color = color_producer(pl))))

#creating feature groups for populations
fgpop = folium.FeatureGroup(name= "Population")

#loading population  json dataset

fgpop.add_child(folium.GeoJson(data=(open("world.json","r",encoding="utf-8-sig").read()),
style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"] < 10000000
else "yellow" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


#adding laayer contrl
map.add_child(fgp)
map.add_child(fgpop)

#adding feature group
map.add_child(folium.LayerControl())

#saving map to html
map.save("Map1.html")
