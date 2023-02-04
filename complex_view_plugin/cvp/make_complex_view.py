from core.models import Graph, Node, Edge
from core.services.visualize import VisualizeService

class ComplexVisualizator(VisualizeService):

  def name(self):
    return "Complex visualizator"

  def identifier(self):
    return "complex_visualizator"

  def get_html(self, graph):
    return self.make_complex_view_str(graph)

  def get_nodes_complex_view(self, graph: Graph) -> str:
    string = "{"
    for node_id in graph.data:
        string = string + node_id + ': {' + "\"id\":" + f"\"{node_id}\","
        for key_data, value in graph.data[node_id].data.items():
            string = string + f"\"{key_data}\":" + f"\"{value}\"" + ','
        string = string + '},'
    string = string + "}"

    return str(string)


  def get_links_complex_view(self, graph: Graph) -> str:
      string = '['
      for node_id in graph.data:
          for edge in graph.data[node_id].edges:
              string = string + '{' + "\"source\":" + \
                  "\"" + edge.first_node + "\"" + ',' + "\"target\":" + \
                  "\"" + edge.second_node + "\"" + '},'
      string = string + ']'
      return string


  def make_complex_view_str(self, graph: Graph) -> str:
      string = "let real_nodes = " + self.get_nodes_complex_view(graph) + "\n"
      string = string + "let nodes = " + self.get_nodes_complex_view(graph) + "\n"
      string = string + "let links = " + self.get_links_complex_view(graph) + "\n"
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
          .linkDistance(400)
          .charge(-10000)
          .start();

        let svg = d3.select("svg")
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
          makeComplexView(d);
        });


        // this function make node of graph
        function makeComplexView(d) {
          let width = 150;
          let numberOfAttribute = Object.keys(real_nodes[d.id]).length;
          
          let textSize = 10;
          let height = (numberOfAttribute==1)?textSize+2:numberOfAttribute*2*(textSize+2);

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

          let i=0;
          for(let attribute in real_nodes[d.id])
          {
          i++;
          let atr = attribute + ":" + real_nodes[d.id][attribute];
          // Prikaz naziva kategorije
          d3.select("g#"+d.id)
              .append("text")
              .attr("x",0)
              .attr("y",20+i*textSize)
              .attr("text-anchor","start")
              .attr("font-size",textSize)
              .attr("font-family","sans-serif")
              .attr("fill","black")
              .text(atr);
          }

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
