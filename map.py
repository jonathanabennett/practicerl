from Tile import Tile

class Map():
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.grid = [[Tile(True)
                 for x in range(height)]
                for y in range(width)]
    
  def lookup(self, x, y):
    return self.grid[x][y]

  def get_neighbors(self,x,y):
    ret = []
    for t in self.grid[range(x-1,x+1)][range(y-1,y+1)]:
      ret.append(t)
    return ret