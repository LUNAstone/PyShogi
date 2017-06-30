Shogi test example
------------------
OOP used on:
- Board
- Piece (and the subclasses of it)
- Player (used to store their name and their droppable pieces)


The Game
--------
Shogi is an ancient Japanese varient of chess, it is from the same family as theoriginal 'Shatranj' game.
It's name translated is "Generals' Game".
It is played on a 9x9 board, with each player controlling 21 pieces with the goal being to checkmate the opponent's king.
An additional rule to this is that any captured pieces may be played on the board, taking a turn, as your own.


The Pieces
----------
The pieces are as follows:
- **Fuhyou** (歩兵), abbreviated to Fu (歩).
  It's name translates to 'foot soldier'.
  
  It moves like the pawn in western chess,  but it cannot be moved two places on its first move, and it takes vertically.
  
  There are a few other limitations on the pawn, which limit it's ability to be dropped in some circumstances:
  1) It cannot be placed on the same file which has another unpromoted pawn of your own
  2) It cannot be placed directly checkmating the king
  3) It cannot be placed in a location from which it cannot move.
  
  It promotes into the **Tokin** (と金), shortened to To (と), which moves like the **Kinshou**.
  
  Tokin translates to 'Reaches Gold'.


- **Kyousha** (香車), abbreviated to Kyo (香).
  Translated, it's name is 'Incense Chariot', and is often called the 'lance'.
  
  It is able to *range* forwards, but it cannot move any spaces diagonally, leftwards, rightwards or backwards.
  
  This piece also cannot be placed on the back rank.
  
  It promotes to the **Narikyou** (成香) which is translated as 'Promoted Chariot', and it does not have an abbreviation out of Japanese (杏).
  
  The Narikyou moves like the **Kinshou**.
  
  
- **Keima** (桂馬), or Kei (桂). This translates into 'Cassia Horse'.

  It jumps like the knight in western chess, however it cannot move sideways or backwards, and only forwards.
  
  The Keima must promote if it reaches the back two ranks and cannot be dropped on those.
  
  It promotes to the **Narikei** (成桂), or 'promoted cassia'. It does not have an abbreviation out of Japanese (圭).
  
  The Narikei moves like the **Kinshou**.
  
  
- **Ginshou** (銀將), shortened to Gin (銀). Which translates to 'Silver General'.

  It can move one space diagonally, and one space forwards.
  
  It promotes into the **Narigin** (成銀), or 'promoted silver'. It does not have an abbreviation out of Japanese (全).
  
  The Narigin moves like the **Kinshou**.
  
- **Kinshou** (金將), shortened to Kin(金). Which translates to 'Gold General'.

  It can move one space vertically and horizontally, and it can move one space forwards diagonally on both sides.
  
  The Kinshou cannot promote.
  
- The **Kakugyou** (角行) is a major piece and there is only one of them on each side, it is shortened to **Kaku** (角).
  Translated, it is the 'Angle Mover'.
  
  It acts the same as the bishop in western chess.
