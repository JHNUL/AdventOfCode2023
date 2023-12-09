# Day 9 solution

https://adventofcode.com/2023/day/9

### Part 1

Straightforward implementation of the rules of the problem statement. I managed to mess it up by first taking the absolute difference of the pair of values, but it really was just `num[i]-num[(i-1)]`

### Part 2

Basically the same, just with the first values of the produced new lines and subtracting instead of adding.
