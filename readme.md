# Technical test for leboncoin.fr

## Goal

Find the largest square on a map that avoids obstacles.
A file is given as an input, the first line has the following info :
    - number of lines of the map
    - the "empty" character
    - the "obstacle" character
    - the "full" character

The program should replace "empty" characters with "full" characters to represend the largest *square* possible.

Whenever several solutions are found, the represented square should be the furthest on the top-left of the map.


## Validity of maps

- Every line should have the same length
- There is at least one line of at least one cell
- The map can only have characters as presented on the first line of the file

Whenever an invalid map is passed into the program, show the following on sys.stderr : `map error` and continue on
to the next map in the list.

## Constraints

- Only use python's standard library
- The program can take 1 or more maps as an input
