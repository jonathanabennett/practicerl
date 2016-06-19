import curses, sys
from math import floor
from player import Player
from thing import Thing
from map import Map
from level import MapGenerator
import logging

logging.basicConfig(filename="game.log", level=logging.DEBUG)
directions = {"North":(-1,0), "South":(1,0), "East":(0,1), "West":(0,-1),
             "NorthWest":(-1,-1), "NorthEast":(-1,1), "SouthWest":(1,-1),
             "SouthEast":(1,1)}

class Game():
  
  self.keybindings = {'h': (self.move_object, (self.things[0], "North")),
                     'j': (self.move_object, (self.things[0], "North")),
                     'g': (self.move_object, (self.things[0], "East")),
                     'k': (self.move_object, (self.things[0], "West")),
                     'y': (self.move_object, (self.things[0], "NorthWest")),
                     'u': (self.move_object, (self.things[0], "NorthEast")),
                     'b': (self.move_object, (self.things[0], "SouthWest")),
                     'n': (self.move_object, (self.things[0], "SouthEast"))
                     'l': (self.look, (self.things[0],))}
  
  def __init__(self, screen):
    self.main = screen
    curses.curs_set(0)
    self.main.scrollok(0)
    self.colorize()
    self.height, self.width = self.main.getmaxyx() #Gets screensize. Split this into its own function called on screen resize
    logging.info(self.height)
    self.height -= 2
    self.width -= 2
    self.main.border(0)
    self.things = []
    self.things.append(Player(int(floor(self.height/2)), #See player.py for
                              int(floor(self.width/2)))) #class description
    self.map = MapGenerator(self.width, self.height, self.things).map
    self.main_loop()
    
  def colorize(self):
    curses.use_default_colors()
    curses.init_pair(1, 191, -1)
    curses.init_pair(2, -1, 250)
    curses.init_pair(3, -1, 235)
    curses.init_pair(4, 107, -1)
    curses.init_pair(5, 131, -1)
    self.color_palette = {}
    self.color_palette["Player"] = 0
    self.color_palette["NPC"] = 1
    self.color_palette["dark_wall"] = 2
    self.color_palette["dark_floor"] = 3
    self.color_palette["Orc"] = 4
    self.color_palette["Troll"] = 5
    
  def main_loop(self):
    #This will catch and handle all keystrokes. Not too happy with if,elif,elif or case. Use a dict lookup eventually
    while 1:
      self.render_all()
      
      c = self.main.getch()
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
  
  def look(self, origin_thing):
    x = origin_thing.x
    y = origin_thing.y
    while 1:
      self.main.addch(x, y, "X")
      c = self.main.getch()
      if c == curses.ENTER:
        for thing in things:
          if x == thing.x and y == thing.y:
            self.main.addstr(self.height-1,1,thing.description)
            return True
      elif ord(c) in ('g','h','j','k','y','u','b','n'):
        x += directions[self.keybindings[ord(c)](1)(1)](0)
        y += directions[self.keybindings[ord(c)](1)(1)](1)
    
  def move_object(self, thing, direction): 
    """I chose to let the Game class handle redraws instead of objects.
    I did this because it will make it easier should I ever attempt to rewrite
    this with libtcod, pygcurses, or even some sort of browser-based thing.
    Display is cleanly separated from obects and map data.
    Objects use the variable name "thing" to avoid namespace collision."""
    curx = thing.x
    cury = thing.y
    newy = thing.y + directions[direction][0]
    newx = thing.x + directions[direction][1]
    if not self.is_blocked(newx, newy):
      logging.info("Not blocked")
      thing.x = newx
      thing.y = newy
      
  def is_blocked(self,x,y):
    if self.map.lookup(x,y).blocked:
      logging.info("Blocked by wall")
      return True
    
    for thing in self.things:
      if thing.blocks and x == thing.x and y == thing.y:
        logging.info("Blocked by %s" % thing.description)
        return True
    return False
  
  def clear_thing(self, y, x, thing):
    """Broken out to handle stacks of things in one location, resurrecting
    things, and other times I don't want to just blit out the whole tile.
    Right now, it just blits the tile though..."""
    self.main.addch(y, x, " ",
                   curses.color_pair(self.color_palette["dark_floor"]))
    
  def render_all(self):
    for y in range(self.map.height):
      for x in range(self.map.width):
        wall = self.map.lookup(x,y).blocked
        if wall:
#          logging.info("Drawing wall at %s, %s" % (str(x), str(y)))
          self.main.addch(y, x, " ",
                         curses.color_pair(self.color_palette["dark_wall"]))
        else:
#          logging.info("Drawing floor at %s, %s" % (str(x), str(y)))
          self.main.addch(y, x, " ",
                         curses.color_pair(self.color_palette["dark_floor"]))
    for thing in self.things:
      self.draw_thing(thing)
    self.draw_thing(self.things[0])
  
  def draw_thing(self, thing):
    self.main.addch(thing.y, thing.x, thing.disp,
                    curses.color_pair(self.color_palette[thing.color]))
    
  def save_game(self):
    sys.exit()

def loop(screen):
  g = Game(screen)
  
if __name__ == "__main__":
  curses.wrapper(loop) #Should I put the main loop outside the Game Object?