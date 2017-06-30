# PyShogi, a version of Shogi made in Python with OOP.
# An explanation of the game can be found in the README.

class Board:
  """ This class defines the board which will be created as a 2D array.
  It will also be able to have some of the piece objects stored onto it.
  """
  
  def __init__(self):
    pass
  

class Player:
  """ Name, an array of pieces they have taken from the enemy.
  The array will contain the type of the piece that they have in their possession
  e.g. [FU, FU, FU, HI]
  After a player has dropped their piece it is removed from the list and put into play
  as their own piece.
  
  """

class Piece:
  """ This is the parent class for all of the different types of pieces.
  They will all have attributes that define their colour, their location,
  and if they have been taken or not.
  """
  
  def __init__(self, owner, locationx, locationy):
    self.owner = owner
    self.locationx = locationx
    self.locationy = locationy
    self.promotion = ""
  
    
  def move(self):
    pass
  
  
  def capture(self):
    pass
  
  
  def drop(self):
    pass