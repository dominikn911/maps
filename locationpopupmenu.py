from kivymd.uix.dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):
    def __init__(self, markets_data):
        super().__init__()

        # Set all of the fields of restaurant data
        headers = "FMID,MarketName,Website,street,city,zip,Season1Date,x,y"
        headers = headers.split(',')

        for i in range(len(headers)):
            attributes_name = headers[i]
            attributes_value = markets_data[i]
            setattr(self, attributes_name, attributes_value)

