from fastapi import FastAPI, Response
from graphviz import Digraph
import io
from typing import List, Optional
from pydantic import BaseModel

class Node(BaseModel):
    id: str
    description: str
    color: Optional[str] = "darkolivegreen3"
    shape: Optional[str] = "box"
    style: Optional[str] = "solid"

class Edge(BaseModel):
    from_node: str
    to_node: str
    color: Optional[str] = "darkolivegreen3"
    style: Optional[str] = "solid"

class GraphStructure(BaseModel):
    nodes: List[Node]
    edges: List[Edge]
    

def get_graph(graph_structure: GraphStructure) -> Digraph:
    dot = Digraph(comment='Mapa Mental')
    for node in graph_structure.nodes:
        dot.node(node.id, node.description, color=node.color, shape=node.shape, style=node.style)
    
    for edge in graph_structure.edges:
        dot.edge(edge.from_node, edge.to_node, color=edge.color, style=edge.style)
    return dot

def generate_mind_map(graph_structure: GraphStructure):
    dot = get_graph(graph_structure)
    img_stream = io.BytesIO()
    img_stream.write(dot.pipe(format='png'))
    img_stream.seek(0)
    with open("test_mind_map.png", "wb") as f:
        f.write(img_stream.read())
    img_stream.seek(0)  # Reset the stream position for reading in Response
    return Response(content=img_stream.read(), media_type="image/png")
