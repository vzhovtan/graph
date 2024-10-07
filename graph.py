from typing import Union

import edge
import node

class Graph:
  def __init__(self, num_nodes: int, undirected: bool=False):
    self.num_nodes: int = num_nodes
    self.undirected: bool = undirected
    self.nodes: list = [node.Node(j) for j in range(num_nodes)]

  def get_edge(self, from_node: int, to_node: int) -> Union[edge.Edge, None]:
    if from_node < 0 or from_node >= self.num_nodes:
      raise IndexError
    if to_node < 0 or to_node >= self.num_nodes:
      raise IndexError
    return self.nodes[from_node].get_edge(to_node)

  def is_edge(self, from_node: int, to_node: int) -> bool:
    return self.get_edge(from_node, to_node) is not None

  def make_edge_list(self) -> list:
    all_edges: list = []
    for node in self.nodes:
      for edge in node.edges.values():
        all_edges.append(edge)
    return all_edges

  def insert_edge(self, from_node: int, to_node: int, weight: float):
    if from_node < 0 or from_node >= self.num_nodes:
      raise IndexError
    if to_node < 0 or to_node >= self.num_nodes:
      raise IndexError
    self.nodes[from_node].add_edge(to_node, weight)
    if self.undirected:
      self.nodes[to_node].add_edge(from_node, weight)

  def remove_edge(self, from_node: int, to_node: int):
    if from_node < 0 or from_node >= self.num_nodes:
      raise IndexError
    if to_node < 0 or to_node >= self.num_nodes:
      raise IndexError
    self.nodes[from_node].remove_edge(to_node)
    if self.undirected:
      self.nodes[to_node].remove_edge(from_node)

  def insert_node(self, label=None) -> node.Node:
    new_node: node.Node = node.Node(self.num_nodes, label=label)
    self.nodes.append(new_node)
    self.num_nodes += 1
    return new_node