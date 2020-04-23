class Coordinate:
    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon

    def __str__(self):
        return "{} : {}".format(self.latitude, self.longitude)

print(Coordinate(7, 77))

print("latitude: {latitude} || longitude: {longitude}".format(Coordinate(7, 77)))


