class UserPoint:
    x = 0.0
    y = 0.0  

class UserPosition:
    userid = 0
    userpoint = None
    @staticmethod
    def parse_position(data):
        res = UserPosition()
        data_arr = data.split(",")
        res.userid = data_arr[0].split(":")[1]
        res.userpoint = UserPoint()
        res.userpoint.x = data_arr[1].split(":")[1]
        res.userpoint.y = data_arr[2].split(":")[1]
        return res

    @staticmethod
    def parse_positions(data):
        res = []
        data = data.replace("[{","")
        data = data.replace("}]","")   
        data = data.split("},{") 
        for pos in data:
            user_position = UserPosition.parse_position(pos)
            res.append(user_position)
        return res

    def __str__(self):
        return f"UserId: {self.userid}, x: {self.userpoint.x}, y: {self.userpoint.y}"


data = "[{id:10,x:10,y:20},{id:5,x:30,y:40},{id:2,x:2,y:7}]"

positions = UserPosition.parse_positions(data)
for pos in positions:
    print(pos)  
