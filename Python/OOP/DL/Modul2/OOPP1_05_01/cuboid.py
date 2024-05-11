class Cuboid:

    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c
        print ("Cuboid has values: ", "a = ", self.a, "b= ", self.b,"c=", self.c)
    def cuboid_volume(self):
        return (self.a * self.b * self.c)
    def cuboid_area(self):
        return 2 * (self.a * self.b + self.b *  self.c + self.a *  self.c)

new_cuboid = Cuboid(10,10,10)
print("Cuboid volume is: ", new_cuboid.cuboid_volume())
print("Cuboid area is: ", new_cuboid.cuboid_area())

