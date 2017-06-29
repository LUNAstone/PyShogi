""" Shogi test example
OOP used on:
- Board
- Piece (and the subclasses of it)
- Player (used to store their name and their droppable pieces)

Shogi (??) is an ancient Japanese varient of chess, it is from the same family as the
original 'Shatranj' game. It's name translated is "Generals' Game". It is played on a
9x9 board, with each player controlling 21 pieces with the goal being to checkmate the
opponent's king. An additional rule to this is that any captured pieces may be played
on the board, taking a turn, as your own.

The pieces are as follows:
- Fuhy? (??), abbreviated to ? (Fu). It moves like the pawn in western chess,
  but it cannot be moved two places on its first move, and it takes vertically.
  There are a few other limitations on the pawn, which limit it's ability to be dropped
  in some circumstance: it cannot be placed on the same file which has another
  unpromoted pawn of your own, it cannot be placed directly checkmating the king,
  and it cannot be placed in a location from which it cannot move.
  It promotes into the Tokin (??), shortened to To (?). It moves like the Kinsh?.
  

By Jamie Land
"""

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