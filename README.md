# PyShogi
OOP used on:
- Board
- Piece (and the subclasses of it)
- Player (used to store their name and their droppable pieces)


## The Game
Shogi is an ancient Japanese varient of chess, it is from the same family as the original 'Shatranj' game.
It's name translated is "Generals' Game".
It is played on a 9x9 board, with each player controlling 21 pieces with the goal being to checkmate the opponent's king.
An additional rule to this is that any captured pieces may be played on the board, taking a turn, as your own.


## The Pieces
The pieces are as follows:
- __P__: **Fuhyou** (歩兵), abbreviated to Fu (歩).
  It's name translates to 'foot soldier'.
  
  It moves like the pawn in western chess,  but it cannot be moved two places on its first move, and it takes vertically.
  
  There are a few other limitations on the pawn, which limit it's ability to be dropped in some circumstances:
  1) It cannot be placed on the same file which has another unpromoted pawn of your own
  2) It cannot be placed directly checkmating the king
  3) It cannot be placed in a location from which it cannot move.
  
  __+P__: It promotes into the **Tokin** (と金), shortened to To (と), which moves like the **Kinshou**.
  
  Tokin translates to 'Reaches Gold'.


- __L__: **Kyousha** (香車), abbreviated to Kyo (香).
  Translated, it's name is 'Incense Chariot', and is often called the 'lance'.
  
  It is able to *range* forwards, but it cannot move any spaces diagonally, leftwards, rightwards or backwards.
  
  This piece also cannot be placed on the back rank.
  
  __+L__: It promotes to the **Narikyou** (成香) which is translated as 'Promoted Chariot', and it does not have an abbreviation out of Japanese (杏).
  
  The Narikyou moves like the **Kinshou**.
  
  
- __N__: **Keima** (桂馬), or Kei (桂). This translates into 'Cassia Horse'.

  It jumps like the knight in western chess, however it cannot move sideways or backwards, only forwards.
  
  The Keima must promote if it reaches the back two ranks and cannot be dropped on those.
  
  __+N__: It promotes to the **Narikei** (成桂), or 'promoted cassia'. It does not have an abbreviation out of Japanese (圭).
  
  The Narikei moves like the **Kinshou**.
  
  
- __S__: **Ginshou** (銀將), shortened to Gin (銀). Which translates to 'Silver General'.

  It can move one space diagonally, and one space forwards.
  
  __S__: It promotes into the **Narigin** (成銀), or 'promoted silver'. It does not have an abbreviation out of Japanese (全).
  
  The Narigin moves like the **Kinshou**.
  

- __G__: **Kinshou** (金將), shortened to Kin(金). Which translates to 'Gold General'.

  It can move one space vertically and horizontally, and it can move one space forwards diagonally on both sides.
  
  The Kinshou cannot promote.
  

- __B__: The **Kakugyou** (角行) is a major piece and there is only one of them on each side, it is shortened to **Kaku** (角).
  Translated, it is the 'Angle Mover'.
  
  It acts the same as the bishop in western chess.

  __+B__: When promoted, the Kakugyou becomes the **Ryuuma** (龍馬), shortened to **Uma** (馬). This is translated as 'Dragon Horse'.

  The Ryuuma can moves like the **Kakugyou**, but it also gains the ability to move one step vertically or horizontally.


- __R__: The **Hisha** (飛車) is a major piece and there is only one of them on each side. It's name is shortened to **Hi** (飛).
  When translated, it's name is the 'Flying Chariot'.

  It acts the same as the rook in western chess.

  __+R__: When promoted, the Hisa becomes the **Ryuou** (龍王), or 'Dragon King' and is shortened to **Ryuu** (龍).

  The Ryuou retains it's horizontal and vertical movement, like in **Hisha** form, but it also gains a single step diagonally.


- __K__: There are two kings in shogi, the **Oushou** (王將) 'King General', shortened to **Ou** (王);
  and the **Gyokushou** (玉將) 'Jewel General', shortened to **Gyoku** (玉).
  There is no difference between these two pieces, but generally the 'better player' (through social status or skill at the game) will play
  with the Oushou.

  Both move in the same way as the king in western chess.


## The Board
In shogi, both sides have control over the three ranks nearest to them, which is where their pieces are. On the closest rank
there is, going from left to right, the Kyousha, the Keima, the Ginshou, the Kinshou, the Oushou (or Gyokushou), Kinshou, Ginshou, Keima, Kyousha.

On the next rank in front of that, there are the Kakugyou and Hisha, with the Kakugyou in front of the left Keima, and the Hisha in front of the right.

And then in front of that is a line of 9 Fuhyou.

The first player (Sente) is displayed on the bottom of the game board, and the second player (Gote) is on the top.
Who goes first is decided by a randomly by the system.

Each square has a number and letter which correlates to it. At the top from the right to the left it counts up from 1,
and on the right, from top to bottom, there are the letters A to I.

So the top left square is 9A and bottom left is 9I, etc.
