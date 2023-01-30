from pathlib import Path
from datetime import datetime
from core.models import Graph, Node, Edge
from core.services.load import LoadService

def timestamp_to_datetime(timestamp):
  return datetime.fromtimestamp(timestamp)

class FileSystemParser(LoadService):

  def name(self):
    return "File system parser"

  def identifier(self):
    return "file_system_parser"

  def load(self, path):
    graph = Graph({})
    self.makeNode(path, graph)
    return graph

  def makeNode(self, path, graph):
    entry = Path(path) # neki Path objekat od putanje, iz njega se vade podfajlovi, podaci i ostalo

    # node_id = str(entry.absolute()) # apsolutna putanja fajla ili foldera je kljuc u recniku u grafu, a i id cvora
    node_id = "id" + str(graph.counter)
    # ovde se inicijalizuje cvor, on moze da bude fajl ili folder, ali svejedno mora da se sacuva u grafu
    # dodaje mu se pocetni edge sa folderom u kom se on nalazi
    node = Node(node_id, [], {
      "path": str(entry.absolute()).replace("\\", "/"),
      "date": timestamp_to_datetime(entry.stat().st_mtime), # ovde moze da se ubace bilo koji podaci, date je primer samo
      "size": entry.stat().st_size, # velicina fajla u bajtovima
      "extension": entry.suffix,
      "type": "folder" if entry.is_dir() else "file",
      "name": entry.name
    })
    graph.counter += 1 # brojac cvorova u grafu, da moze da se proveri da li su svi fajlovi i folderi ubaceni, moze da se izbaci kasnije, nebitan je
    if node.id not in graph.data: # ako node nije u grafu, ubacuje se u njega, posto je ovo stablo, mislim da se nikad nece desiti da vec bude u grafu, ali ajde za svaki slucaj
      graph.data[node.id] = node

    if entry.is_dir(): # ako je folder, onda se prolazi kroz fajlove i foldere tog foldera
      for sub in entry.iterdir():
        other_node = self.makeNode(str(sub.absolute()), graph) # napravi se node za taj element foldera
        id1 = node.id # id tekuceg foldera
        id2 = other_node.id # id fajla ili foldera koji se nalazi u tekucem folderu
        graph.data[node.id].edges.append(Edge(id1, id2, {})) # u edges tekuceg foldera se doda edge sa njegovim podfolderom ili podfajlom
    
    return node


if __name__=="__main__":
  file_system_parser = FileSystemParser()
  graph = file_system_parser.load("D:/Faks/3. Godina/Metodologije razvoja softvera")
  print(graph)