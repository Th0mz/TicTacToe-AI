﻿## TicTacToe
---
#### Demo : 
[<img alt="demo_image" width="1280" src="assets/thumb.png" />](https://www.youtube.com/watch?v=egVbwP_Fw9c)

---
#### Description: <br>
   
- Is the well-known `TicTacToe`, where the player plays against a bot [AI] that *chooses the next move* using the **minimax** algorithm.
<br>

- Using minimax to choose the next best move makes the AI unbeatable, because the TicTacToe its such a simple game it can always calculate the overall best move. 

---

#### The Algorithm [Minimax]:
   
- **Minimax** is a kind of backtracking algorithm (finds *all* solutions for a given board, *choosing the best play* to make at that instance), normally used in games like *TicTacToe* or even *chess* to find the best play.
- This algorithm can be a **little inefficient** just because it needs to calculate *every single possible play* that can occur. But we can use minimize the number of plays needed to calculate using another algorithm `alpha beta pruning`, which its main objective *is not calculate the same play twice*.
   
   <br>

- In minimax there are *2 states*:
    - <u>*The maximizer*</u> : Where we try to get the highest score possible 
    - <u>*The minimizer*</u> : Where we try to get the lowest score possiple

    - The maximizer is the player that is tring to make the optimal move and the minimizer is his opponent which means, *The maximizer* will choose the move that is more advantageous for him, and expects that *The minimizer* plays his best move (the one with the lowest score for the maximizer)

    - A play has more points if it leads the maximizer to win the game and less if it leads him to lose

    <br>

- So in this case what will happen is:
    
    - Given an initial game we determine all the movements that the maximizer can do (it is easy to see this information in a tree graph here the root is the initial game and the leafs is all the possible plays that the maximizer can do)

    - Then we call the minimax function on all of the leafs until, The maximizer wins *[Score +1]* , the minimizer wins *[Score -1]* or there is a Tie *[Score 0]*

    - So when the minimax function was called on all leafs the last ones that where called will have a score and that score will **backtrack** to the root of the tree giving us the best move to play the one with better score

    - The ``backtracking`` works this way, we compare all leafs of some root, and that root will take the score by this rules:
        
        - If the player playing is the minimizer the root should have the lowest score of the leafs

        - If the player playing is the maximizer the root should have the highest score of the leafs

---

#### To improve

The current algorithm only uses the minimax algorithm to get to the perfect move, but given that this algorithm is a bruteforce one (tries all possible combinations) it some times can be a little slow to find the first and second moves.

One thing I could do (and probably will in a near future) is applying alpha-beta pruning which is a way to cut some of the prossible combinations.

Alpha-beta pruning don't allow to calculate solutions for duplicate boards or even boards that are so bad that can be discarded as a possibility.

---
