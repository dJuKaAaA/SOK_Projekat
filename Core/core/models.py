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

  def search(self, term):
    g = Graph({})

    for node_id in self.data:
      node = self.data[node_id]
      if self.search_check(term, node):
        g.data[node_id] = node

    for node_id in g.data:
      node = g.data[node_id]
      node.edges = list(filter(lambda x: x.second_node in g.data, node.edges))

    return g

  def search_check(self, term, node):
    for key in node.data:
      if term in str(node.data[key]):
        return True
    return False

