# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:22:25 2020

@author: HUY QUYEN NGO (Jason)
Project: Path-Planning for ground vehicle using A* algorithm
"""

from helpers import Map, load_map_10, load_map_40, show_map
import math

%load_ext autoreload
%autoreload 2


map_10 = load_map_10()
show_map(map_10)

map_10.intersections

# this shows that intersection 0 connects to intersections 7, 6, and 5
map_10.roads[0] 

# This shows the full connectivity of the map
map_10.roads

# map_40 is a bigger map than map_10
map_40 = load_map_40()
show_map(map_40)

# parameters in the function call.
show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])











class PathPlanner():
    """Construct a PathPlanner Object"""
    def __init__(self, M, start=None, goal=None):
        """ """
        self.map = M
        self.start= start
        self.goal = goal
        self.closedSet = self.create_closedSet() if goal != None and start != None else None
        self.openSet = self.create_openSet() if goal != None and start != None else None
        self.cameFrom = self.create_cameFrom() if goal != None and start != None else None
        self.gScore = self.create_gScore() if goal != None and start != None else None
        self.fScore = self.create_fScore() if goal != None and start != None else None
        self.path = self.run_search() if self.map and self.start != None and self.goal != None else None
    
    def reconstruct_path(self, current):
        """ Reconstructs path after search """
        total_path = [current]
        while current in self.cameFrom.keys():
            current = self.cameFrom[current]
            total_path.append(current)
        return total_path
    
    def _reset(self):
        """Private method used to reset the closedSet, openSet, cameFrom, gScore, fScore, and path attributes"""
        self.closedSet = None
        self.openSet = None
        self.cameFrom = None
        self.gScore = None
        self.fScore = None
        self.path = self.run_search() if self.map and self.start and self.goal else None

    def run_search(self):
        """ """
        if self.map == None:
            raise(ValueError, "Must create map before running search. Try running PathPlanner.set_map(start_node)")
        if self.goal == None:
            raise(ValueError, "Must create goal node before running search. Try running PathPlanner.set_goal(start_node)")
        if self.start == None:
            raise(ValueError, "Must create start node before running search. Try running PathPlanner.set_start(start_node)")

        self.closedSet = self.closedSet if self.closedSet != None else self.create_closedSet()
        self.openSet = self.openSet if self.openSet != None else  self.create_openSet()
        self.cameFrom = self.cameFrom if self.cameFrom != None else  self.create_cameFrom()
        self.gScore = self.gScore if self.gScore != None else  self.create_gScore()
        self.fScore = self.fScore if self.fScore != None else  self.create_fScore()

        while not self.is_open_empty():
            current = self.get_current_node()

            if current == self.goal:
                self.path = [x for x in reversed(self.reconstruct_path(current))]
                return self.path
            else:
                self.openSet.remove(current)
                self.closedSet.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in self.closedSet:
                    continue    # Ignore the neighbor which is already evaluated.

                if not neighbor in self.openSet:    # Discover a new node
                    self.openSet.add(neighbor)
                
                # The distance from start to a neighbor
                #the "dist_between" function may vary as per the solution requirements.
                if self.get_tentative_gScore(current, neighbor) >= self.get_gScore(neighbor):
                    continue        # This is not a better path.

                # This path is the best until now. Record it!
                self.record_best_path_to(current, neighbor)
        print("No Path Found")
        self.path = None
        return False
    
    
    
    
    
def create_closedSet(self):
    """ Creates and returns a data structure suitable to hold the set of nodes already evaluated"""
    # return a data structure suitable to hold the set of nodes already evaluated
    closedSet = set()
    return closedSet


def create_openSet(self):
    """ Creates and returns a data structure suitable to hold the set of currently discovered nodes 
    that are not evaluated yet. Initially, only the start node is known."""
    if self.start != None:
        # return a data structure suitable to hold the set of currently discovered nodes 
        # that are not evaluated yet. Make sure to include the start node.
        discovered_nodes = set()
        discovered_nodes.add(self.start)
        return discovered_nodes
    
    raise(ValueError, "Must create start node before creating an open set. Try running PathPlanner.set_start(start_node)")
    
    
def create_cameFrom(self):
    """Creates and returns a data structure that shows which node can most efficiently be reached from another,
    for each node."""
    # return a data structure that shows which node can most efficiently be reached from another,
    # for each node. 
    cameFrom = {}
    return cameFrom
    

def create_gScore(self):
    """Creates and returns a data structure that holds the cost of getting from the start node to that node, 
    for each node. The cost of going from start to start is zero."""
    # return a data structure that holds the cost of getting from the start node to that node, for each node.
    # for each node. The cost of going from start to start is zero. The rest of the node's values should 
    # be set to infinity.
    gScore = {}
    for i in range(len(self.map.intersections)):
        gScore[i] = float('inf')
    gScore[self.start] = 0
    return gScore
    

def create_fScore(self):
    """Creates and returns a data structure that holds the total cost of getting from the start node to the goal
    by passing by that node, for each node. That value is partly known, partly heuristic.
    For the first node, that value is completely heuristic."""
    # return a data structure that holds the total cost of getting from the start node to the goal
    # by passing by that node, for each node. That value is partly known, partly heuristic.
    # For the first node, that value is completely heuristic. The rest of the node's value should be 
    # set to infinity.
    fScore = {}
    for i in range(len(self.map.intersections)):
        fScore[i] = float('inf')
    fScore[self.start] = self.heuristic_cost_estimate(self.start)
    return fScore


def set_map(self, M):
    """Method used to set map attribute """
    self._reset(self)
    self.start = None
    self.goal = None
    # Set map to new value. 
    self.map = M
    return None


def set_start(self, start):
    """Method used to set start attribute """
    self._reset(self)
    # Set start value. Remove goal, closedSet, openSet, cameFrom, gScore, fScore, 
    # and path attributes' values.
    self.start = start
    self.goal = None
    self.closedSet = None
    self.openSet = None
    self.cameFrom = None
    self.gScore = None
    self.fScore = None
    self.path = None
    return None
    

def set_goal(self, goal):
    """Method used to set goal attribute """
    self._reset(self)
    # Set goal value. 
    self.goal = goal
    return None


def is_open_empty(self):
    """returns True if the open set is empty. False otherwise. """
    # Return True if the open set is empty. False otherwise.
    if len(self.openSet) == 0:
        return True
    return False


def get_current_node(self):
    """ Returns the node in the open set with the lowest value of f(node)."""
    # Return the node in the open set with the lowest value of f(node).
    
    temp = {}
    for node in self.openSet:
        temp[node] = self.calculate_fscore(node)
    return min(temp, key=temp.get)


def get_neighbors(self, node):
    """Returns the neighbors of a node"""
    # Return the neighbors of a node
    return set(self.map.roads[node])


def get_gScore(self, node):
    """Returns the g Score of a node"""
    # Return the g Score of a node
    return self.gScore.get(node)


def distance(self, node_1, node_2):
    """ Computes the Euclidean L2 Distance"""
    # Compute and return the Euclidean L2 Distance
    distance1 = self.map.intersections[node_1][0] - self.map.intersections[node_2][0]
    distance2 = self.map.intersections[node_1][1] - self.map.intersections[node_2][1]
    return math.sqrt(distance1**2 + distance2**2)


def get_tentative_gScore(self, current, neighbor):
    """Returns the tentative g Score of a node"""
    # Return the g Score of the current node 
    # plus distance from the current node to it's neighbors
    return (self.get_gScore(current) + self.distance(current,neighbor))



def heuristic_cost_estimate(self, node):
    """ Returns the heuristic cost estimate of a node """
    # Return the heuristic cost estimate of a node
    return self.distance(node,self.goal)


def calculate_fscore(self, node):
    """Calculate the f score of a node. """
    # Calculate and returns the f score of a node. 
    # F = G + H
    return (self.get_gScore(node) + self.heuristic_cost_estimate(node))
    

def record_best_path_to(self, current, neighbor):
    """Record the best path to a node """
    # Record the best path to a node, by updating cameFrom, gScore, and fScore
    self.cameFrom[neighbor] = current
    self.gScore[neighbor] = self.get_tentative_gScore(current,neighbor)
    self.fScore[current] = self.calculate_fscore(current)
    return None

    
# Associates implemented functions with PathPlanner class
PathPlanner.create_closedSet = create_closedSet
PathPlanner.create_openSet = create_openSet
PathPlanner.create_cameFrom = create_cameFrom
PathPlanner.create_gScore = create_gScore
PathPlanner.create_fScore = create_fScore
PathPlanner.set_map = set_map
PathPlanner.set_start = set_start
PathPlanner.set_goal = set_goal
PathPlanner.is_open_empty = is_open_empty
PathPlanner.get_current_node = get_current_node
PathPlanner.get_neighbors = get_neighbors
PathPlanner.get_gScore = get_gScore
PathPlanner.distance = distance
PathPlanner.get_tentative_gScore = get_tentative_gScore
PathPlanner.heuristic_cost_estimate = heuristic_cost_estimate
PathPlanner.calculate_fscore = calculate_fscore
PathPlanner.record_best_path_to = record_best_path_to


planner = PathPlanner(map_40, 5, 34)
path = planner.path
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)
    

# Visualize your the result of the above test! You can also change start and goal here to check other paths
start = 5
goal = 34

show_map(map_40, start=start, goal=goal, path=PathPlanner(map_40, start, goal).path)
    

from test import test

test(PathPlanner)