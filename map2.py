import folium
import pandas


data = pandas.read_csv("volc.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
nam = list(data["NAME"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el  in zip(lat, lon, nam, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=str(nm), 
    fill_color=color_producer(el), color='white', fill_opacity=0.7))


fgm = folium.FeatureGroup(name="Me")
fgm.add_child(folium.Marker(location=[-33.823122, 18.659841], popup="Colin, Mamma, Dad, Joz & Zaine", icon=folium.Icon(color='green')))
fgm.add_child(folium.Marker(location=[-33.986132, 23.721752], popup="OakHurst", icon=folium.Icon(color='green')))
fgm.add_child(folium.Marker(location=[-26.015249, 28.143749], popup="Rosande", icon=folium.Icon(color='green')))
fgm.add_child(folium.Marker(location=[-24.936555, 30.834425], popup="Pa & Sonja", icon=folium.Icon(color='green')))
fgm.add_child(folium.Marker(location=[-32.907618, 19.067255], popup="Beaverlac", icon=folium.Icon(color='green')))
fgm.add_child(folium.Marker(location=[-30.863230, 30.371253], popup="Seagull", icon=folium.Icon(color='green')))
fgm.add_child(folium.Marker(location=[52.092160, 5.258347], popup="Claire & kids", icon=folium.Icon(color='green')))


fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
            style_function=lambda x: {'fillColor':'green' 
            if x['properties']['POP2005'] < 10000000 
            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
            else 'red'}))



map.add_child(fgv)
map.add_child(fgm)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map2.html")