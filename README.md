# The Game of Life

*Python 3*
*Object-oriented program*
*Cellular Automata*

####AUTHOR:
Tom M Logan
www.tomlogan.co.nz

####BASED ON:
The game of life code is as described in
http://natureofcode.com/book/chapter-7-cellular-automata/
by Daniel Shiffman

##THE GAME OF LIFE:

**Here are the rules of life:**

- Death. If a cell is alive (state = 1) it will die (state becomes 0) under the following circumstances.
  - Overpopulation: If the cell has four or more alive neighbors, it dies.
  - Loneliness: If the cell has one or fewer alive neighbors, it dies.
- Birth. If a cell is dead (state = 0) it will come to life (state becomes 1) if it has exactly three alive neighbors (no more, no less).
- Stasis. In all other cases, the cell state does not change. To be thorough, let’s describe those scenarios.
  - Staying Alive: If a cell is alive and has exactly two or three live neighbors, it stays alive.
  - Staying Dead: If a cell is dead and has anything other than three live neighbors, it stays dead.

There are 8 neighbours.