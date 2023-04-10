# 2D-Puzzle-Traversal

This program finds the shortest path from a source to a destination on a 2-D puzzle of an arbitrary size
by utilizing queues and breadth-first searches.

The 2-D Puzzle board is formatted like the following inside "Puzzle.py":<br />
    ['-','-','-','-','-'],<br />
    ['-','-','#','-','-'],<br />
    ['-','-','-','-','-'],<br />
    ['#','-','#','#','-'],<br />
    ['-','#','-','-','-']

'-' represents empty space while '#' represents obstacles.
The source and destination are represented as tuple coordinates like "(2,0)" for example.

You can modify the board in "Puzzle.py" by changing the size of the board and changing the amount of empty spaces or obstacles.

You can also modify the source and destination values.

## Directions:

First, open "Puzzle.py" with a text editor to modify the puzzle board, source value, and destination value you want solved.

Once you have confirmed the three values above, then run command "python Puzzle.py" or "python3 Puzzle.py" to begin solving the puzzle.

A terminal should output the puzzle board that has been solved, the list of coordinates forming the shortest path from the source
coordinate to destination coordinate, and a string of directions where 'R' is right, 'L' is left, 'D' is down, and 'U' is up.
