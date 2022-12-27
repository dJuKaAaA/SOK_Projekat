from django.db import models

# Create your models here.

class Node:
  def __init__(self, identifier, edges, data):
    self.id = identifier
    self.edges = edges
    self.data = data
    
class Edge:
  def __init__(self, first_node, second_node, data=None):
    self.first_node = first_node
    self.second_node = second_node
    self.data = data

class Graph:
  def __init__(self, nodes, edges, data=None):
    self.nodes = nodes
    self.edges = edges
    self.data = data
