import curses, sys
from math import floor
from player import Player
from thing import Thing
from map import Map

class Game():
  def __init__(self, screen):
    self.main = screen
    curses.curs_set(0)
    self.colorize()
    self.height, self.width = self.main.getmaxyx() #Gets screensize. Split this into its own function called on screen resize
    self.map = Map(self.height, self.width)
    self.main.border(0)
    self.things = []
    self.things.append(Player(int(floor(self.height/2)), #See player.py for
                              int(floor(self.width/2)))) #class description
    self.things.append(Thing(int(floor(self.height/2)-5),
                             int(floor(self.width/2)),
                             disp="@",
                             color=self.color_palette["NPC"],
                             description="A lowly peasant"))
    self.main_loop()
    
  def colorize(self):
    curses.use_default_colors()
    curses.init_pair(1, 191, -1)
    curses.init_pair(2, -1, 250)
    curses.init_pair(3, -1, 235)
    self.color_palette = {}
    self.color_palette["Player"] = 0
    self.color_palette["NPC"] = 1
    self.color_palette["dark_wall"] = 2
    self.color_palette["dark_floor"] = 3
    
  def main_loop(self):
    #This will catch and handle all keystrokes. Not too happy with if,elif,elif or case. Use a dict lookup eventually
    while 1:
      self.render_all()
        
      c = self.main.getch()
      self.main.addstr(self.height-1,1,str(c))
      if c == ord('p'):
        self.main.addstr(self.height-1,1,self.things[0].description)
      if c == curses.KEY_UP:
        self.move_object(self.things[0], "North", self.map)
      if c == curses.KEY_DOWN:
        self.move_object(self.things[0], "South", self.map)
      if c == curses.KEY_LEFT:
        self.move_object(self.things[0], "West", self.map)
      if c == curses.KEY_RIGHT:
        self.move_object(self.things[0], "East", self.map)
      elif c == ord('q'):
        self.save_game()
      elif c == curses.KEY_HOME:
        x = y = 0
        
  def move_object(self, thing, direction, map): 
    """I chose to let the Game class handle redraws instead of objects.
    I did this because it will make it easier should I ever attempt to rewrite
    this with libtcod, pygcurses, or even some sort of browser-based thing.
    Display is cleanly separated from obects and map data.
    Objects use the variable name "thing" to avoid namespace collision."""
    curx = thing.x
    cury = thing.y
    newy, newx = thing.move(direction, map)
    if cury != newy or curx != newx:
      self.clear_thing(cury, curx, thing)
      self.draw_thing(thing)
      return True
    else:
      return False
  
  def clear_thing(self, y, x, thing):
    """Broken out to handle stacks of things in one location, resurrecting
    things, and other times I don't want to just blit out the whole tile.
    Right now, it just blits the tile though..."""
    self.main.addch(y, x, " ",
                   curses.color_pair(self.color_palette["dark_floor"]))
    
  def render_all(self):
    for y in range(self.height-1):
      for x in range(self.width-1):
        wall = self.map.lookup(x,y).blocked
        if wall:
          self.main.addch(y, x, " ",
                         curses.color_pair(self.color_palette["dark_wall"]))
        else:
          self.main.addch(y, x, " ",
                         curses.color_pair(self.color_palette["dark_floor"]))
    for thing in self.things:
      self.draw_thing(thing)
  
  def draw_thing(self, thing):
    self.main.addch(thing.y, thing.x, thing.disp,
                    curses.color_pair(thing.color))
    
  def save_game(self):
    sys.exit()

def loop(screen):
  g = Game(screen)
  
if __name__ == "__main__":
  curses.wrapper(loop) #Should I put the main loop outside the Game Object?