import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

featureGroup = folium.FeatureGroup(name="My Map")
for lat, lon, elevation in zip(latitude, longitude, elevation):
    featureGroup.add_child(folium.CircleMarker(
        location=[lat, lon],
        radius=6,
        popup=str(elevation) + " meters",
        fill_opacity=0.7,
        color='grey'))
featureGroup.add_child(folium.GeoJson(data=(open("world.json", 'r', encoding='utf-8-sig').read()),
                                      style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000 
                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(featureGroup)
map.add_child(folium.LayerControl())
map.save("Map1.html")
