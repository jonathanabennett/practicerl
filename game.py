import curses, sys
from math import floor
from player import Player

class Game():
  def __init__(self):
    self.main = curses.initscr()
    self.height, self.width = self.main.getmaxyx()
    self.main.border(0)
    curses.noecho()
    self.main.keypad(1)
    self.player = Player(int(floor(self.height/2)), int(floor(self.width/2)))
    self.main.addch(self.player.y, self.player.x, self.player.disp)
    self.main_loop()
   
  def main_loop(self):
    while 1:
      c = self.main.getch()
      if c == ord('p'):
        self.main.addstr(1,1,"It works!")
      elif c == ord('q'):
        self.save_game()
      elif c == curses.KEY_HOME:
        x = y = 0
  
  def save_game(self):
    curses.nocbreak()
    self.main.keypad(0)
    curses.echo()
    curses.endwin()
    sys.exit()

if __name__ == "__main__":
  g = Game()