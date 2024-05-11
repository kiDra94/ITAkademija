import datetime

class GpsPoint:
    date    = 0
    lat     = 0
    lon     = 0
    time    = 0
    imei    = 0
    @staticmethod
    def parse(msg):
        parts = msg.split(",")    
        res = GpsPoint() if len(parts) <= 5 else HGpsPoint() 
        res.date    = datetime.datetime.strptime(parts[0],"%d%m%Y")
        res.lat     = float(parts[1])
        res.lon     = float(parts[2])
        res.time    = datetime.datetime.strptime(parts[3],"%H%M%S")
        res.imei    = parts[4]
        return res

    def __str__(self):
        return f"GpsPoint {self.date} {self.lat} {self.lon} {self.time} {self.imei}"

class HGpsPoint(GpsPoint):
    def __str__(self):
        return f"HGpsPoint {self.date} {self.lat} {self.lon} {self.time} {self.imei}"

msg = "22052014,44.756364,20.412598,051230,123143124122"
pt = GpsPoint.parse(msg)
print(pt)