class Square_obj(object):

    def __init__(self,one_side, second_side):
        self.one_side = one_side
        self.second_side = second_side

    def perimetrs(self):
        perimeter = self.one_side*2+self.second_side*2
        return perimeter

    def square(self):
        square = self.second_side*self.one_side
        return square


class Dot(object):

    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

    def distance_to_start(self):
        distance = (self.X**2+self.Y**2)**0.5
        return distance

    def distance_to_dot(self, Dot):
        distance = ((self.X-Dot.X)**2+(self.Y-Dot.Y)**2)**0.5
        return distance

if __name__ == "__main__":
    room = Square_obj(2,3)
    print(room.perimetrs())
    print(room.square())
    a = Dot(1,4)
    b = Dot(3,7)
    print(a.distance_to_start())
    print(a.distance_to_dot(b))
