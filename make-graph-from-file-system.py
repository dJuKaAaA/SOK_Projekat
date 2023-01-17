

from pathlib import Path
from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

class Node:
  def __init__(self, identifier, edges, data):
    self.id = identifier
    self.edges = edges
    self.data = data

  def __str__(self):
    return self.id + " - " + str(self.data)
    
class Edge:
  def __init__(self, first_node, second_node, data=None):
    self.first_node = first_node
    self.second_node = second_node
    self.data = data

  def __str__(self):
    return f"({self.first_node} -- {self.second_node} -- {self.data})"

class Graph:
  def __init__(self, data, counter):
    self.data = data
    self.counter = counter

def makeNode(path, graph, old):
  entry = Path(path) # neki Path objekat od putanje, iz njega se vade podfajlovi, podaci i ostalo

  node_id = str(entry.absolute()) # apsolutna putanja fajla ili foldera je kljuc u recniku u grafu, a i id cvora

  # ovde se inicijalizuje cvor, on moze da bude fajl ili folder, ali svejedno mora da se sacuva u grafu
  # dodaje mu se pocetni edge sa folderom u kom se on nalazi
  node = Node(node_id, [Edge(node_id, old, {})], {
    "date": convert_date(entry.stat().st_mtime) # ovde moze da se ubace bilo koji podaci, date je primer samo
  })
  graph.counter += 1 # brojac cvorova u grafu, da moze da se proveri da li su svi fajlovi i folderi ubaceni, moze da se izbaci kasnije, nebitan je
  if node.id not in graph.data: # ako node nije u grafu, ubacuje se u njega, posto je ovo stablo, mislim da se nikad nece desiti da vec bude u grafu, ali ajde za svaki slucaj
    graph.data[node.id] = node

  if entry.is_dir(): # ako je folder, onda se prolazi kroz fajlove i foldere tog foldera
    for sub in entry.iterdir():
      other_node = makeNode(str(sub.absolute()), graph, node.id) # napravi se node za taj element foldera
      id1 = node.id # id tekuceg foldera
      id2 = other_node.id # id fajla ili foldera koji se nalazi u tekucem folderu
      graph.data[node.id].edges.append(Edge(id1, id2, {})) # u edges tekuceg foldera se doda edge sa njegovim podfolderom ili podfajlom
  
  return node

if __name__ == "__main__":

  graph = Graph({}, 0)

  # ova funkcija pravi graf za folder iz prvog argumenta, ali mora da se unese i njegov nadfolder zbog prve iteracije, verovatno moze lako da se sredi kad se ubaci u graf, ali nebitno je sad
  makeNode("D:/Faks/3. Godina/Mobilne aplikacije/Vezbe primeri", graph, "D:/Faks/3. Godina/Mobilne aplikacije")
  print(graph.counter) # ovde moze da se proveri da li su svi fajlovi i folderi izbrojani, desni klik na folder iz prvog argumenta i saberi fajlove i foldere i dodaj 1 i treba da bude jednako counteru, dodaje se da racuna i izabrani folder

  # for node_id in graph.data:
  #   print("*******")
  #   print(node_id)
  #   node = graph.data[node_id]
  #   print(node.data)
  #   print("*******")
  #   for edge in node.edges:
  #     print(edge)
  #   print("------")

  