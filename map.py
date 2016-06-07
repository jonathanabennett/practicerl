from Tile import Tile

class Map():
  def __init__(self, height, width):
    self.grid = [[Tile(False)
                 for y in range(height)]
                for x in range(width)]
    self.grid[30][22].blocked = True
    self.grid[30][22].block_sight = True
    self.grid[50][22].blocked = True
    self.grid[50][22].block_sight = True
    
  def lookup(self, x, y):
    return self.grid[x][y]