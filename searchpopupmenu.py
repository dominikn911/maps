from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import certifi
from kivy.clock import  Clock
from restaurantmapview import RestaurantMapView

class SearchPopupMenu(MDInputDialog):
    title = 'Search by Adress'
    text_button_ok = 'Search'
    pub_names = ["pub", "pubs", "puby"]
    restaurant_names = ["restauracja", "restauracje", "restaurant", "restaurants"]
    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

#    def open(self):
#        super.open()
#        Clock.schedue_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        result = [x.strip() for x in address.split(',')]
        objectType = 0
        if result[0].lower() in self.restaurant_names or result[0].lower() in self.pub_names:
            objectType = 1 if result[0].lower() in self.restaurant_names else 2
            city = result[1]
            name = result[2] if len(result) > 2 else "none"
        else:
            city = result[0]
            name = result[1] if len(result) > 1 else "none"
        RestaurantMapView.set_address(city, name, objectType)

        self.geocode_get_lat_lon(city)

    def geocode_get_lat_lon(self, address):
        with open('api_key.txt', 'r') as f:
            api_key = f.read()
        address = parse.quote(address)
        url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext=%s&gen=9&apiKey=%s"%(address, api_key)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)
#        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where)

    def success(self, urlrequest, result):
        print("success")
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)

    def error(self, urlrequest, result):
        print("error")
        print(result)

    def failure(self, urlrequest, result):
        print("failure")
        print(result)
