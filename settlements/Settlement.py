from constants import ED
from gdpc import geometry as geo


class Settlement:

    def __init__(self, name, location, size):
        self.name = name
        self.location = location
        self.size = size
        self.buildings = []
        self.worldSlice = ED.loadWorldSlice(geo.Rect(location, size))

    def settle(self):
        """
        Settle the settlement, astract method
        """
        pass
