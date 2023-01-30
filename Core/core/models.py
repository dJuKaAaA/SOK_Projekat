from django.db import models
from datetime import datetime

# Create your models here.

class Node:
  def __init__(self, identifier, edges, data={}):
    self.id = identifier
    self.edges = edges
    self.data = data

  def __str__(self):
    ret = ""
    for key in self.data:
      ret += str(key) + ": " + str(self.data[key]) + "\n"
    return ret
    
class Edge:
  def __init__(self, first_node, second_node, data=None):
    self.first_node = first_node
    self.second_node = second_node
    self.data = data

  def __str__(self) -> str:
    return str(self.first_node) + " - " + str(self.second_node)

class Graph:
  def __init__(self, data):
    self.data = data
    self.counter = 0

  def add_node(self, node):
    self.data[node.id] = node
    self.counter += 1

  def __str__(self):
    ret = ""
    for node_id in self.data:
      for edge in self.data[node_id].edges:
        ret += str(edge) + "\n"
      ret += "----------------------------------\n"
    return ret

  
