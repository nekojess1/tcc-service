from pydantic import BaseModel
from typing import List

class Node(BaseModel):
    id: str
    description: str
    hit_percentage: int

class Edge(BaseModel):
    from_node: str
    to_node: str

class GraphData(BaseModel):
    nodes: List[Node]
    edges: List[Edge]
