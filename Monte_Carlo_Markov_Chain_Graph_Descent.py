import numpy as np
import csv
import networkx as nx
import random


class MCMC_stochastic_descent(object):

    """
    Runs the Monte Carlo Markov Chain Graph Descent algorithms
    for finding local and global minimums on a network
    """

    def __init__(self, G):

        self.G = G
        self.num_nodes = G.number_of_nodes()
        self.num_edges = G.number_of_edges()


    def local_minimum(self, node, max_iter=100):

        """
        Finds a local minimum on the network beginning at the given node.

        Parameters:
            node: The node to begin the algorithm at
            max_iter: Iteration during which to algorithm.

        Returns:
            node: a local minimum for the network
        """

        x = 0
        while (x < max_iter):

            nbs_node = [i for i in self.G[node]]
            new_node = random.choice(nbs_node)

            if new_node <= node:
                node = new_node
            x += 1

        return node

    def global_minimum(self, node, lamb=0.5, max_iter=1000):
        """
        Attempts to fine a global minimum on network beginning at the given node.
        Success is more likely for higher iterations and proper choice of lambda.
        Choice of affects is the likelihood moving to a node with a higher value.

        Parameters:
            node: The node to begin the algorithm at
            lambd: Choice of lambda, from 0 to 1
            max_iter: Iteration during which to algorithm.

        Returns:
            node: a local minimum for the network

        """
        x = 0
        while(x < max_iter):

            nbs_node = [i for i in self.G[node]]
            new_node = random.choice(nbs_node)

            if new_node <= node:
                node = new_node

            elif lamb ** (new_node-node) > random.random():
                node = new_node

            x += 1

        return node
