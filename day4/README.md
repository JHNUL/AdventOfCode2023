# Day 4 solution

### Part 1

There are two sets of numbers for each line in the input. We need the size of the intersection of these sets to count the points. Since they double on each matching number, the final value of the card is 1 << (n-1) where n is the size of the intersection, except for no matches where it is 0.

![part 1](day4p1.png)

### Part 2

Now we keep the amount of cards won in a new array where we can accumulate the amounts when parsing each line of the input. The final answer is the sum of the numbers in the cards array.

![part 2](day4p2.png)