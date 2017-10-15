from Car import *

class Point:
  def __init__(self, x, y):
    self.x, self.y = x, y

  def __str__(self):
    return "{}, {}".format(self.x, self.y)

  def __neg__(self):
    return Point(-self.x, -self.y)

  def __add__(self, point):
    return Point(self.x+point.x, self.y+point.y)

  def __sub__(self, point):
    return self + -point
p1 = Point(0,0) #Note that I use coordinates instead of distance to make it easier
p2 = input("Select destination")#Selects the destination where you want to go
if p2 == "North":
        p1.y+=3
        print("Binus")
elif p2 == "North-east":
        p1.y+=3
        p1.x+=2
        print("PIM")
elif p2 == "North-west":
        p1.y+=5
        p1.x+=-5
        print("Kemang")
elif p2 == "South":
        p1.y+=-3
        print("Prapanca")
elif p2 == "West":
        p1.x+=-4
        print("Grand Indonesia")
elif p2 == "East":
        p1.x+=5
        print("Monas")
elif p2 == "South-east":
        p1.x+=9
        p1.y+=-1
        print("TMNI")
elif p2 == "South-west":
        p1.x+=-3
        p1.y+=-7
        print("Alam Sutera")
print(p1.x,p1.y)
driver = Point(0,0)
def pos():
    print(driver.x, driver.y)
while True:
    driver_move = input("Move")
    if driver_move == "N":
        driver.y+=1
        pos()
    elif driver_move == "S":
        driver.y+=-1
        pos()
    elif driver_move == "E":
        driver.x+=1
        pos()
    elif driver_move == "W":
        driver.x+=-1
        pos()
    elif driver_move =="Cancel":
        break
    else:#Resets the position
        driver = Point(0,0)
    if driver.x==p1.x and driver.y==p1.y:
         print("You have reached the destination")
         break
