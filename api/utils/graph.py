from fastapi import FastAPI, Response
from graphviz import Digraph
import io
from typing import List, Optional
from pydantic import BaseModel
import plotly.express as px

class Node(BaseModel):
    id: str
    description: str
    hit_percentage: int
    color: Optional[str] = "darkolivegreen3"
    shape: Optional[str] = "box"
    style: Optional[str] = "solid"

class Edge(BaseModel):
    from_node: str
    to_node: str
    color: Optional[str] = "grey70"
    style: Optional[str] = "solid"

class GraphStructure(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

def get_color_from_percentage(percentage):
    colorscale = px.colors.sequential.Plasma
    color_idx = int((percentage / 100) * (len(colorscale) - 1))
    return colorscale[color_idx]

def get_graph(graph_structure: GraphStructure) -> Digraph:
    dot = Digraph(comment='Mapa Mental', engine='fdp')

    for node in graph_structure.nodes:
        dot.node(node.id, node.description, color = get_color_from_percentage(node.hit_percentage), shape=node.shape, style=node.style)
    for edge in graph_structure.edges:
        dot.edge(edge.from_node, edge.to_node, color=edge.color, style=edge.style)
    print(dot)
    return dot
    
def generate_mind_map(graph_structure: GraphStructure):
    dot = get_graph(graph_structure)
    img_stream = io.BytesIO()
    img_stream.write(dot.pipe(format='pdf'))
    img_stream.seek(0)
    with open("test_mind_map.pdf", "wb") as f:
        f.write(img_stream.read())
    img_stream.seek(0)  # Reset the stream position for reading in Response
    return Response(content=img_stream.read(), media_type="application/pdf")

