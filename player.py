from thing import Thing
directions = {"North":(-1,0), "South":(1,0), "East":(0,1), "West":(0,-1)}

class Player(Thing):
  """Player will eventually subclass a MapObject class. That class will have every variable objects on the map have in common.
  Definitely that will include x,y coordinates, a description, and a display character."""
  def __init__(self,y,x, disp="@", color="Player", description="A stout warrior of courage and might", blocks=True):
    self.y = y
    self.x = x
    self.disp = "@"
    self.color = color
    self.description = description
    self.blocks = blocks

#  def move(self, direction, map): #Map will be for collision detection. Put here to simplify wall walking implementation
#    newy = self.y + directions[direction][0]
#    newx = self.x + directions[direction][1]
#    if not map.lookup(newx,newy).blocked:
#      self.x = newx
#      self.y = newy
#    return self.y, self.x