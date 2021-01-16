# RA-Project

This is a resolution of the assignment from chapter 10.6 of the Mitzenmatcher-Upfal book "Probability and Computing - Randomized Algorithms and Probabilistic Analysis"

The focus of this project is about the Minimum Spanning Tree of a complete, undirected graph with n nodes, where each edge has a random weight, a real number chosen uniformly between [0,1].
The main goal is to estimate how the expected weight of the minimum spanning tree grows as a function of n for such graphs.

This project was implemented using Python v3.8.5

## Execution

To run on a machine with Python 3 installed, from the RA-Project directory, type:

    $ python Main.py

The parameters (Number of nodes, seed, and whether or not to exclude big edges according to k(n)) can be easily edited on lines 87, 88 and 89 of the Main.py file
