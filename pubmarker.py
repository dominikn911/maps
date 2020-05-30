from locationpopupmenu import LocationPopupMenu
from kivy.garden.mapview import MapMarkerPopup
#from kivy_garden.mapview import MapMarkerPopup


class PubMarker(MapMarkerPopup):
    source = "pub_marker.png"
    pub_data = []

    def on_release(self):
        #open up the locationpopupmenu
        menu = LocationPopupMenu(self.pub_data)
        menu.size_hint = [.8, .9]
        menu.open()
