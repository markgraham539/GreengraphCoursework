
import googleMapsLib 
import pngLib
import miscLib
import matplotlib
import matplotlib.pyplot as plt

def greengraphMain(start,end):
  #Get green levels for spaced intervals between locations
  [pngLib.count_green_in_png(googleMapsLib.map_at(*location,zoom=10,satellite=True))
              for location in miscLib.location_sequence(
                  googleMapsLib.geolocate(start),
                  googleMapsLib.geolocate(end),10)]

  #Code for displaying green map of a png
  '''
  ### "save"

  matplotlib.use('Agg')

  with open('green.png','w') as green:
      green.write(pngLib.show_green_in_png(googleMapsLib.map_at(*london_location,
          zoom=10,satellite=True)))'''

  #Plot and save
  plt.plot([
      pngLib.count_green_in_png(
          googleMapsLib.map_at(*location,zoom=10,satellite=True))
            for location in miscLib.location_sequence(
                googleMapsLib.geolocate(start),
                googleMapsLib.geolocate(end),10)])
  plt.savefig('greengraph.png')