#thing.py

class Thing():
  
  def __init__(self,y,x, disp="@", color=0, description="A stout warrior of courage and might", blocks=True):
    self.y = y
    self.x = x
    self.disp = "@"
    self.color = color
    self.description = description
    self.blocks = blocks