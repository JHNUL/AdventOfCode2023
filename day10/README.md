# Day 10 solution

https://adventofcode.com/2023/day/10

### Part 1

Starting from S traverse the matrix according to these rules:
- if movement is possible, go to the adjacent cell and mark current cell visited
- if movement is not possible, we are at the end of the loop
- furthest point in the loop is the size of visited cells divided by two

Keep visited cells in a set for fast lookups.

### Part 2

