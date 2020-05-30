import folium

map = folium.Map(location=[-28.743699, 24.745200], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[-33.823122, 18.659841], popup="Colin, Mamma, Dad, Joz & Zaine", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[-33.986132, 23.721752], popup="OakHurst", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[-26.015249, 28.143749], popup="Rosande", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[-24.936555, 30.834425], popup="Pa & Sonja", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[-32.907618, 19.067255], popup="Beaverlac", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[-30.863230, 30.371253], popup="Seagull", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[52.092160, 5.258347], popup="Claire & kids", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map1.html")