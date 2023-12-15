# Day 11 solution

### Part 1

Idea: make one iteration over the matrix, save each galaxy position such that we can identify both the coordinates of the galaxies and the row numbers $i$ and column numbers $k$ which contain no galaxies.

Then make a search to the coordinates to loop through every pair and count their Manhattan-distance ($|\Delta x - \Delta y|$). Then see how many rows and columns with no galaxies are in between the coordinates and add that number to the distance.

This way we do not need to manually enlarge the matrix before resolving the distances.

### Part 2

Part 1 solution worked for this as well with no additional complexity, since the only additional thing needed was a multiplier to the number of empty rows and columns in between the coordinates.