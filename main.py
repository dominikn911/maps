from kivymd.app import MDApp
from restaurantmapview import RestaurantMarker
import sqlite3
from searchpopupmenu import SearchPopupMenu

class MainApp(MDApp):
    connection = None
    pubConnection = None
    cursor = None
    pubCursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.priamry_palette = 'BlueGrey'
        # Initialize GPS
        # connect to database
        self.connection = sqlite3.connect("restaurant.db")
        self.pubConnection = sqlite3.connect("pub.db")
        self.cursor = self.connection.cursor()
        self.pubCursor = self.pubConnection.cursor()
        #initialize popupmenu
        self.search_menu = SearchPopupMenu()
    pass

MainApp().run()
