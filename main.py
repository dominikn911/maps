from kivymd.app import MDApp
from marketsmapview import MarketsMapView
import sqlite3
from searchpopupmenu import SearchPopupMenu
from gpshelper import GpsHelper

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.priamry_palette = 'BlueGrey'
        # Initialize GPS
        GpsHelper().run()
        # connect to database
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()
        #initialize popupmenu
        self.search_menu = SearchPopupMenu()
    pass

MainApp().run()
