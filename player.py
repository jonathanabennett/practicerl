class Player():
  """Player will eventually subclass a MapObject class. That class will have every variable objects on the map have in common.
  Definitely that will include x,y coordinates, a description, and a display character."""
  def __init__(self,y,x, disp="@", description="A stout warrior of courage and might"):
    self.y = y
    self.x = x
    self.disp = "@"
    self.description = description
