import folium
import pandas

def set_color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

path = "E:\\my_folder\\python\\Python_repo\\App2\\App2_src\\"
data = pandas.read_csv(path + "Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(tiles = "Mapbox bright")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, color = "grey", fill_color = set_color(el),
                                     fill = True, fill_opacity = 0.7,  popup = str(el) + " m" ))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = (open(path + "world.json", 'r', encoding = 'utf-8-sig').read()),
                            style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000
                                                        else "orange" if x["properties"]["POP2005"] < 600000000
                                                        else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("E:\\my_folder\\map.html")
