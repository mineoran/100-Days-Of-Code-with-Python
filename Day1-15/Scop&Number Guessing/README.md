### In this project; We will learn what local and global scop means

### Local (or function) Scope:

**Local scope is the code block or body of any Python function or lambda expression. This Python scope contains the names that you define inside the function. These names will only be visible from the code of the function. It’s created at function call, not at function definition, so you’ll have as many different local scopes as function calls. In short, variables defined in a function are called local variables. What we mean by local variables is that the variables are specific to the function.**

### Global Scope:
**They are variables declared outside of a function or in a global scope in Python, so we can access global variables inside and outside the function.**
**We will examine local and global scopes in our Number Guessing project.**

## Our project rules is:

#### Allow the player to submit a guess for a number between 1 and 100.
#### Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
#### If they got the answer correct, show the actual answer to the player.
#### Track the number of turns remaining.
#### If they run out of turns, provide feedback to the player. 
#### Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
