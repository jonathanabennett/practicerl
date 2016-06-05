#curses test
import curses, sys
class Game():
  def __init__(self):
    self.height = 40
    self.width = 50
    self.main = curses.initscr()
    self.main.border(0)
    curses.noecho()
    self.main.keypad(1)
    self.main.addch(self.height/2, self.width/2, "@")
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
  