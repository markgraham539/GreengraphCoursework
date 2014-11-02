#Test googleMapsLib
import googleMapsLib

#Test known result of geolocation
def test_geoLocate():
	actual_londonLocation = (51.5073509, -0.1277583)
	test_londonlocation = googleMapsLib.geolocate('London')
	assert actual_londonLocation == test_londonlocation

#Test known result for getting url of london actual_londonLocation
def test_mapAt():
	testMapResponse=googleMapsLib.map_at(51.5072, -0.1275, zoom=10);
	actualMapResponse = 'http://maps.googleapis.com/maps/api/staticmap?style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&center=51.5072%2C-0.1275&sensor=false&zoom=10&size=400x400'	
	assert testMapResponse.url == actualMapResponse