from thing import Thing

class Orc(Thing):
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.disp = "o"
    self.color = "Orc"
    self.description = "An angry Orc."
    self.blocks = True
    
    
    
    
class Troll(Thing):
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.disp = "T"
    self.color = "Troll"
    self.description = "A slobbering Troll."
    self.blocks = True