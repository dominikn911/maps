from kivymd.app import MDApp
from restaurantmapview import RestaurantMarker
import sqlite3
from searchpopupmenu import SearchPopupMenu

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.priamry_palette = 'BlueGrey'
        # Initialize GPS
        # connect to database
        self.connection = sqlite3.connect("restaurant.db")
        self.cursor = self.connection.cursor()
        #initialize popupmenu
        self.search_menu = SearchPopupMenu()
    pass

MainApp().run()
