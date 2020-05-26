from kivy.clock import Clock
from kivy.app import App
from restaurantmarker import RestaurantMarker
from kivy.garden.mapview import MapView
#from kivy_garden.mapview import MapView




class RestaurantMapView(MapView):
    getting_restaurant_timer = None
    market_names = []
    def start_getting_restaurant_in_fov(self):
        # After one second get yhe markets in the field of view
        try:
            self.getting_restaurant_timer.cancel()
        except:
            pass

        self.getting_restaurant_timer = Clock.schedule_once(self.get_restaurant_in_fov, 1)

    def get_restaurant_in_fov(self, *args):
        # get refernece to main app and datebase cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM markets WHERE x > %s AND x <%s AND y > %s AND y < %s"%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        restaurant = app.cursor.fetchall()
        print(restaurant)
        for market in restaurant:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)

    def add_market(self, market):
        #create market marker
        lat, lon = market[8], market[7]
        marker = RestaurantMarker(lat=lat, lon=lon)
        marker.market_data = market
        #add the market marker to map
        self.add_widget(marker)
        #Keep track of the marker name
        name = market[1]
        self.market_names.append(name)
