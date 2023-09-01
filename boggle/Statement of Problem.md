# Boggle Challenge

<sub>Posted on November 4, 2019 Posted in
[Computer Science](https://www.101computing.net/category/computer-science/),
[Python - Advanced](https://www.101computing.net/category/python-advanced/),
[Python Challenges](https://www.101computing.net/category/python-challenges/)</sub>

Boggle is a word game based on a 4×4 grid of 16 letters. Each time the game is played a
new grid is generated. In the real game this is done by shaking a cube that contains 16
letter dice. The The aim of the game is to find words that can be constructed from
sequentially adjacent letters from the 4×4 grid. “Adjacent” letters are those
horizontally, vertically, and diagonally neighbouring. Words must be at least three
letters long, may include singular and plural (or other derived forms) separately, but
may not use the same letter from the grid more than once per word.

A scoring system can be used based on the number of words identified and by adding the
number of letters in each word.

For this challenge you will re-create a single-player game of Boggle using a step by
step approach.

## Step 1: Generating and displaying a random 4×4 grid

Your first task is to write a script that will randomly generated a 4×4 grid containing
16 letters randomly picked from the alphabet. Note that you can use **ASCII values** for
letter A (ASCII value 65) to Z (ASCII value 90) to generate a random letter as follows:

```python
import random
letter=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
```

A 4×4 grid could be defined as a 2D array (a list of lists in Python). For instance, the
following code uses two nested for loops to generate a 2D array filled with 16 letters
“A”.

```python
grid = []
for row in range(0,4):
   grid.append([])
   for col in range(0,4):
       grid[row].append("A")
print(grid)
```

Your task is to adapt the above code to fill the grid with random letters rather than
just using letter “A”.

Then you will need to complete the code to display the content of the grid using the
right format: the output should look like a 4×4 grid. (Tip: you will need to use
**nested loops** once more time!)

## Step 2: Inputting and validating words

The next step is to let the user input a word that they spotted on the grid. You will
need your program to decide if the word is a valid word that can be generated using
adjacent letters from the grid. (and making sure the same letter cannot be used mote
than once).

## Step 3: Scoring system

Finally you may let the user enter several words, and calculate a total score by adding
the length of all valid words that the user will spot (making sure they do not enter the
same word more than once).
