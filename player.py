directions = {"North":(-1,0), "South":(1,0), "East":(0,1), "West":(0,-1)}

class Player():
  """Player will eventually subclass a MapObject class. That class will have every variable objects on the map have in common.
  Definitely that will include x,y coordinates, a description, and a display character."""
  def __init__(self,y,x, disp="@", description="A stout warrior of courage and might"):
    self.y = y
    self.x = x
    self.disp = "@"
    self.description = description

  def move(self, direction, map=[]): #Map will be for collision detection. Put here to simplify wall walking implementation
    newy = self.y + directions[direction][0]
    newx = self.x + directions[direction][1]
    if True:
      self.x = newx
      self.y = newy
    return self.y, self.x