# Day 8 solution

https://adventofcode.com/2023/day/8

### Part 1

The input format is straightforward to parse into an adjacency list after which navigating it in a loop from the starting node "AAA" until "ZZZ" is reached is simple. The expectation from the problem statement is that there is a path to "ZZZ".


### Part 2

I first tried doing multiple paths in parallel with a collection of nodes transitioning to another collection. This of course ended up being nowhere near the right approach because the number of iterations needed blew right up into the stratosphere. After some thinking and avoiding the temptation of seeing how others had approached this problem I vaguely remembered some other problem of counting the meeting point of multiple looping pointers in a cyclical graph. Key discovery here was noticing that the ghosts each started looping over a distinct target node such that the loop length was the amount of steps from the beginning to first encounter of the target. After that it was a matter of getting the lowest common multiple and luckily pythons math library accommodated.
