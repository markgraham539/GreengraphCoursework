### "geolocation"
import googleMapsLib 

london_location=googleMapsLib.geolocate("London")
print london_location

### "URL"
map_response=googleMapsLib.map_at(51.5072, -0.1275, zoom=10)
url=map_response.url
print url

### "png"
import pngLib


print pngLib.count_green_in_png(googleMapsLib.map_at(*london_location))

### "visualise"




import miscLib
### "points"
[pngLib.count_green_in_png(googleMapsLib.map_at(*location,zoom=10,satellite=True))
            for location in miscLib.location_sequence(
                googleMapsLib.geolocate("London"),
                googleMapsLib.geolocate("Birmingham"),
                10)]


### "save"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
with open('green.png','w') as green:
    green.write(pngLib.show_green_in_png(googleMapsLib.map_at(*london_location,
        zoom=10,satellite=True)))

plt.plot([
    pngLib.count_green_in_png(
        googleMapsLib.map_at(*location,zoom=10,satellite=True))
          for location in miscLib.location_sequence(
              googleMapsLib.geolocate("London"),
              googleMapsLib.geolocate("Birmingham"),10)])
plt.savefig('greengraph.png')