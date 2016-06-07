#curses test
import curses, sys
from math import floor
class Game():
  def __init__(self):
    self.main = curses.initscr()
    self.height, self.width = self.main.getmaxyx()
    self.main.border(0)
    curses.noecho()
    self.main.keypad(1)
    self.main.addch(int(floor(self.height/2)), int(floor(self.width/2)), "@")
    self.main_loop()
   
  def main_loop(self):
    while 1:
      c = self.main.getch()
      if c == ord('p'):
        self.main.addstr(0,0,"It works!")
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
#myscreen = curses.initscr()

#myscreen.border(0)
#myscreen.addstr(12, 25, "Python curses in action!")
#myscreen.refresh()
#while 1:
#    c = myscreen.getch()
#    if c == ord('p'):
#        myscreen.addstr(1,1,"It works!")
#    elif c == ord('q'):
#        break  # Exit the while()
#    elif c == curses.KEY_HOME:
#        x = y = 0

#curses.endwin()

if __name__ == "__main__":
  g = Game()
  