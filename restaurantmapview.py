from kivy.clock import Clock
from kivy.app import App
from restaurantmarker import RestaurantMarker
from pubmarker import PubMarker
from kivy.garden.mapview import MapView
#from kivy_garden.mapview import MapView




class RestaurantMapView(MapView):
    getting_restaurant_timer = None
    market_names = []
    pub_names = []
    cityUpdated = False
    city = "nocity"
    name = "none"
    objectType = 0
    market_markers = []
    pub_markers = []

    def replaceNonAscii(self, strToCheck):
        newstr = ""
        specialSign = "�"
        for ch in strToCheck:
            if ord(ch) >= 128:
                newstr += specialSign
            else:
                newstr += ch
        return newstr

    def start_getting_restaurant_in_fov(self):
        # After one second get yhe markets in the field of view
        try:
            self.getting_restaurant_timer.cancel()
        except:
            pass

        self.getting_restaurant_timer = Clock.schedule_once(self.get_restaurant_in_fov, 1)

    def get_restaurant_in_fov(self, *args):

        if RestaurantMapView.cityUpdated:
            self.clear_markers()
            RestaurantMapView.cityUpdated = False

        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        city = self.replaceNonAscii(self.city)
        #sql_statement = "SELECT * FROM markets WHERE x > %s AND x <%s AND y > %s AND y < %s AND city = '%s'"%(min_lon, max_lon, min_lat, max_lat, city)

        #restaurants
        if self.objectType == 0 or self.objectType == 1:
            sql_statement = "SELECT * FROM markets WHERE city = '%s'" %city
            if self.name != "none":
                mName = self.replaceNonAscii(self.name)
                sql_statement = "SELECT * FROM markets WHERE city = '%s' AND MarketName = '%s'" %(city, mName)
            app.cursor.execute(sql_statement)
            restaurant = app.cursor.fetchall()
            for market in restaurant:
                name = market[1]
                if name in self.market_names:
                    continue
                else:
                    self.add_market(market)
        #pubs
        if self.objectType == 0 or self.objectType == 2:
            sql_statement = "SELECT * FROM pub WHERE city = '%s'" % self.city
            if self.name != "none":
                sql_statement = "SELECT * FROM pub WHERE city = '%s' AND MarketName = '%s'" % (self.city, self.name)
            app.pubCursor.execute(sql_statement)
            pubs = app.pubCursor.fetchall()
            for pub in pubs:
                name = pub[1]
                if name in self.pub_names:
                    continue
                else:
                    self.add_pub(pub)

    def add_market(self, market):
        #create market marker
        lat, lon = market[8], market[7]
        self.market_markers.append(RestaurantMarker(lat=lat, lon=lon))
        market = ['None' if v is None else v for v in market]
        self.market_markers[-1].market_data = market
        #add the market marker to map
        self.add_widget(self.market_markers[-1])
        #Keep track of the marker name
        name = market[1]
        self.market_names.append(name)

    def add_pub(self, pub):
        #create pub marker
        lat, lon = pub[8], pub[7]
        self.pub_markers.append(PubMarker(lat=lat, lon=lon))
        pub = ['None' if v is None else v for v in pub]
        self.pub_markers[-1].pub_data = pub
        #add the pub marker to map
        self.add_widget(self.pub_markers[-1])
        # Keep track of the marker name
        name = pub[1]
        self.pub_names.append(name)


    def clear_markers(self):
        for marker in self.market_markers:
            self.remove_widget(marker)
        self.market_markers.clear()
        self.market_names.clear()

        for marker in self.pub_markers:
            self.remove_widget(marker)
        self.pub_markers.clear()
        self.pub_names.clear()

    @staticmethod
    def set_address(city, name, objectType):
        RestaurantMapView.cityUpdated = True
        RestaurantMapView.city = city
        RestaurantMapView.name = name
        RestaurantMapView.objectType = objectType

