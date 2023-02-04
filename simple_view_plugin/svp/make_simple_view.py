
from core.models import Graph, Node, Edge
from core.services.visualize import VisualizeService

class SimpleVisualizator(VisualizeService):

  def name(self):
    return "Simple visualizator"

  def identifier(self):
    return "simple_visualizator"

  def get_html(self, graph):
    return self.make_simple_view_str(graph)

  def make_simple_view(self, graph: Graph):
      nodes = {}
      for node_id in graph.data:
          nodes[node_id] = {
              "id": node_id,
              "name": node_id
          }

      links: list[dict[str, Node]] = []
      for node_id in graph.data:
          for edge in graph.data[node_id].edges:
              links.append({
                  "source": edge.first_node,
                  "target": edge.second_node
              })

      return nodes, links

  def get_nodes_simple_view(self, graph: Graph) -> str:
      string = "{"
      for node_id in graph.data:
          string = string + node_id + \
              ':' '{' + "\"id\":" + f"\"{node_id}\"" + '},'
      string = string + '}'
      print(string)

      return str(string)

  def get_links_simple_view(self, graph: Graph) -> str:
      string = '['
      for node_id in graph.data:
          for edge in graph.data[node_id].edges:
              string = string + '{' + "\"source\":" + \
                  "\"" + str(edge.first_node) + "\"" + ',' + "\"target\":" + \
                  "\"" + str(edge.second_node) + "\"" + '},'
      string = string + ']'
      print(string)
      return string


  def make_simple_view_str(self, graph: Graph) -> str:
      string = "let nodes = " + self.get_nodes_simple_view(graph) + "\n"
      string = string + "let links = " + self.get_links_simple_view(graph) + "\n"
      string = string + """
  
        links.forEach(function(link) {
            link.source = nodes[link.source];
            link.target = nodes[link.target];
        });

        let force = d3.layout
          .force()
          .size([400, 400])
          .nodes(d3.values(nodes))
          .links(links)
          .on("tick", tick)
          .linkDistance(300)
          .charge(-10000)
          .start();

        let svg = d3.select("#graph-view").select("svg")
              .call(d3.behavior.zoom().on("zoom", function () {
                svg.attr("transform", "translate(" + d3.event.translate + \
                        ")" + " scale(" + d3.event.scale + ")")
              })).append("g");

        //arrow
        svg.append("svg:defs").append("svg:marker")
          .attr("id", "triangle")
          .attr("refX", 6)
          .attr("refY", 6)
          .attr("markerWidth", 30)
          .attr("markerHeight", 30)
          .attr("markerUnits", "userSpaceOnUse")
          .attr("orient", "auto")
          .append("path")
          .attr("d", "M 0 0 12 6 0 12 3 6")
          .style("fill", "black");


        let link = svg
          .selectAll(".link")
          .data(links)
          .enter()
          .append("line")
          .attr("marker-end", "url(#triangle)")
          .attr("class", "link");

        let node = svg
          .selectAll(".node")
          .data(force.nodes()) //add
          .enter()
          .append("g")
          .attr("class", "node")
          .attr("id", function (d) {
            return d.id;
          })
          .on("click", function () {
            nodeClick(this);
          });


        d3.selectAll(".node").each(function (d) {
          makeSimpleView(d);
        });


        // this function make node of graph
        function makeSimpleView(d) {
          let width = 150;
          let height = 50;
          let textSize = 10;

          // draw square
          d3.select("g#" + d.id)
            .append("rect")
            .attr("x", 0)
            .attr("y", 0)
            .attr("width", width)
            .attr("height", height)
            .attr("class","node");


          // display node name
          d3.select("g#" + d.id)
            .append("text")
            .attr("x", width / 2)
            .attr("y", 10)
            .attr("font-size", textSize)
            .attr("class","name")
            .text(d.id);

          // display separator
          d3.select("g#" + d.id)
            .append("line")
            .attr("x1", 0)
            .attr("y1", textSize + 2)
            .attr("x2", width)
            .attr("y2", textSize + 2)
            .attr("class","separator")

        }

        function nodeClick(el) {
          alert("ID: " + el.id);
          openTreeNodeOnClickFromMainView(el.id);
        }

        function tick(e) {

          node
            .attr("transform", function (d) {
              return "translate(" + d.x + "," + d.y + ")";
            }).call(force.drag);

          link
            .attr("x1", function (d) {
              return d.source.x;
            })
            .attr("y1", function (d) {
              return d.source.y;
            })
            .attr("x2", function (d) {
              return d.target.x;
            })
            .attr("y2", function (d) {
              return d.target.y;
            });

            syncMiniMapMovement();
        }

        initMiniMap(links, force);
  """
      return string
