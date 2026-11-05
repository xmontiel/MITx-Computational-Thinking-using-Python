# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:16:06 2026

@author: Xuan
"""

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        super().__init__(src,dest)
        self.weight = weight

    def getWeight(self):
        # Your code here
        return self.weight

    def __str__(self):
        # Your code here
        return str(self.src) + "->" + str(self.dest) + " (" + str(self.weight) + ")"
    