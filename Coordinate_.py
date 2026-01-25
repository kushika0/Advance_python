class Coordinate:
    def __init__(self,x,y):
        self.cod_x= x
        self.cod_y= y

    def __str__(self):
        return '<{}{}>'.format(self.cod_x,self.cod_y)
    
    def eucldian_distance(self,other):
        return ((self.cod_x-other.cod_x)**2 + (self.cod_y-other.cod_y)**2)**0.5
    
    def distance_origin(self):
        return((self.eucldian_distance(Coordinate(0,0))))
    

class Line:
    def __init__(self,a,b,c):
        self.A= a
        self.B = b
        self.C = c

    def __str__(self):
        return '{}x+{}y+{}'.format(self.A,self.B,self.C)
    
    def point_on_line(line,point):
        if line.A*point.cod_x +line.B*point.cod_y+line.C==0:
            return "lies on line"
        else:
            return "does not lie on the line"
        
    def shortest_distance(line,point):
        return abs(line.A*point.cod_x+line.B*point.cod_y+line.C)/(line.A**2+line.B**2)**0.5
    
obj= Coordinate(8,4)
obj2= Coordinate(2,3)

print(obj.distance_origin())

l1 = Line(1,2,3)
print(l1)
print(l1.shortest_distance(obj))
