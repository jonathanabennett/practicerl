import curses, sys
from math import floor
from player import Player

class Game():
  def __init__(self):
    self.main = curses.initscr()
    self.height, self.width = self.main.getmaxyx() #Gets screensize. Split this into its own function called on screen resize
    self.main.border(0)
    curses.noecho()
    curses.curs_set(0) #hide flashing cursor
    self.main.keypad(1) #Enables keystrokes like KEY_UP, KEY_DOWN, etc
    self.player = Player(int(floor(self.height/2)), int(floor(self.width/2))) #See player.py for class description
    self.main.addch(self.player.y, self.player.x, self.player.disp) #Make this a draw_creature function later
    self.main_loop()
   
  def main_loop(self):
    #This will catch and handle all keystrokes. Not too happy with if,elif,elif or case. Use a dict lookup eventually
    while 1:
      c = self.main.getch()
      self.main.addstr(self.height-1,1,str(c))
      if c == ord('p'):
        self.main.addstr(self.height-1,1,self.player.description)
      if c == curses.KEY_UP:
        self.move_object(self.player, "North")
      if c == curses.KEY_DOWN:
        self.move_object(self.player, "South")
      if c == curses.KEY_LEFT:
        self.move_object(self.player, "West")
      if c == curses.KEY_RIGHT:
        self.move_object(self.player, "East")
      elif c == ord('q'):
        self.save_game()
      elif c == curses.KEY_HOME:
        x = y = 0
  def move_object(self, thing, direction):
    curx = thing.x
    cury = thing.y
    newy, newx = thing.move(direction)
    if cury != newy or curx != newx:
      self.main.addch(cury, curx, " ")
      self.main.addch(newy, newx, thing.disp)
      return True
    else:
      return False
  def save_game(self):
    curses.nocbreak() #Step 1 to restore normal terminal function
    self.main.keypad(0) #Step 2 to restore normal terminal function
    curses.echo() #Step 3 to restore normal termainal function 
    curses.endwin() #Sep 4 to restore normal terminal function. These 4 must be called before exit or the terminal goes weird.
    sys.exit()

if __name__ == "__main__":
  g = Game() #Should I put the main loop outside the Game Object?