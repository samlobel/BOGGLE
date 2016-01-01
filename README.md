# Boggle solver

Basic pseudocode solver:

Have two functions: is prefix and is word.
Initialize board into graph
DFS, starting from every point at every step ask is prefix, is word?
If word, add to found set. If not prefix, end run there.
Add on to DFS as long as that letter-square has not been seen before

