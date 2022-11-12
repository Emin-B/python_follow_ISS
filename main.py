import time
import folium
import requests


iss_list = []
m = folium.Map()

while True:
    iss = requests.get("http://api.open-notify.org/iss-now.json").json()
    iss_list.append(
        [iss["iss_position"]["latitude"],
         iss["iss_position"]["longitude"] 
        ]
    )
    for lat, lon in iss_list:
        folium.Marker(
            location=[lon, lat],
            popup="Longitude : " + str(lon) + "<br>" + "Latitude : " + str(lat),
            icon=folium.Icon(color="blue")
        ).add_to(m)
    time.sleep(1)
    m.save("c:/Users/Emin/OneDrive/Formation/Python/service web/index.html")