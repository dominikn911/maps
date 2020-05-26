from locationpopupmenu import LocationPopupMenu
from kivy.garden.mapview import MapMarkerPopup
#from kivy_garden.mapview import MapMarkerPopup


class RestaurantMarker(MapMarkerPopup):
    source = "marker.png"
    market_data = []

    def on_release(self):
        #open up the locationpopupmenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8, .9]
        menu.open()
