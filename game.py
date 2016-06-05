import curses, sys
from math import floor
from player import Player
from thing import Thing

class Game():
  def __init__(self, screen):
    self.main = screen
    curses.curs_set(0)
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
      curses.init_pair(i, i, -1);
#    self.colors = {} #Format: Coder_Friendly_Name: init_pair_number. Not yet implemented
    self.height, self.width = self.main.getmaxyx() #Gets screensize. Split this into its own function called on screen resize
    self.main.border(0)
    self.things = []
    self.things.append(Player(int(floor(self.height/2)), int(floor(self.width/2))))#See player.py for class description
    self.things.append(Thing(int(floor(self.height/2)-5), int(floor(self.width/2)), disp="@", color=191, description="A lowly peasant"))
    self.main_loop()
    
  def colorize(self):
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
      curses.init_pair(i,i,-1)
    self.color_palette = {}
    self.color_palette["Player"] = 0
    self.color_palette["NPC"] = 191
    self.color_palette["dark_wall"] = 240
    self.color_palette["dark_floor"] = 250
  def main_loop(self):
    #This will catch and handle all keystrokes. Not too happy with if,elif,elif or case. Use a dict lookup eventually
    while 1:
      for thing in self.things:
        self.draw_thing(thing)
        
      c = self.main.getch()
      self.main.addstr(self.height-1,1,str(c))
      if c == ord('p'):
        self.main.addstr(self.height-1,1,self.things[0].description)
      if c == curses.KEY_UP:
        self.move_object(self.things[0], "North")
      if c == curses.KEY_DOWN:
        self.move_object(self.things[0], "South")
      if c == curses.KEY_LEFT:
        self.move_object(self.things[0], "West")
      if c == curses.KEY_RIGHT:
        self.move_object(self.things[0], "East")
      elif c == ord('q'):
        self.save_game()
      elif c == curses.KEY_HOME:
        x = y = 0
        
  def move_object(self, thing, direction): 
    """I chose to let the Game class handle redraws instead of objects.
    I did this because it will make it easier should I ever attempt to rewrite
    this with libtcod, pygcurses, or even some sort of browser-based thing.
    Display is cleanly separated from obects and map data.
    Objects use the variable name "thing" to avoid namespace collision."""
    curx = thing.x
    cury = thing.y
    newy, newx = thing.move(direction)
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
    self.main.addch(y, x, " ")
  
  def draw_thing(self, thing):
    self.main.addch(thing.y, thing.x, thing.disp, curses.color_pair(thing.color))
    
  def save_game(self):
    sys.exit()

def loop(screen):
  g = Game(screen)
  
if __name__ == "__main__":
  curses.wrapper(loop) #Should I put the main loop outside the Game Object?