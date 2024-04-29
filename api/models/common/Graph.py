from typing import List
from pydantic import BaseModel

class Node(BaseModel):
    id: str
    content: str

class Edge(BaseModel):
    source: str
    target: str

class Graph(BaseModel):
    nodes: List[Node]
    edges: List[Edge]