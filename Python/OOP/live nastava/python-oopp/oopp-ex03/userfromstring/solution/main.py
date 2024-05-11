class User:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.score = ""

    @staticmethod
    def parse(data):
        data_arr = data.split("-")
        res = User()
        res.id      = data_arr[0]
        res.name    = data_arr[1]
        res.score   = data_arr[2]
        return res

data = "1-Peter-150"
user = User.parse(data)
print(user.id,user.name,user.score)
