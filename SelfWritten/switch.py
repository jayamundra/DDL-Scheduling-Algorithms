from node import *

class Switch:
  def __init__(self, id, node_count, cpu_p_node, gpu_p_node, memory_p_node):
    self.id = id
    self.node_count = node_count
    self.cpu_count = node_count * cpu_p_node
    self.gpu_count = node_count * gpu_p_node
    self.total_memory = node_count * memory_p_node
    self.free_memory = self.total_memory
    self.nodes_list = dict()

    #creating the switch
    for i in range(self.node_count):
      self.nodes_list[i] = Node(i, cpu_p_node, gpu_p_node, memory_p_node)
      
    
  def free_gpu_count(self):
    count = 0
    for _, node in self.nodes_list.items():
      count += node.free_gpus
    return count
      
  def calc_free_memory(self):
    free_mem = 0
    for node in self.nodes_list.values():
      free_mem += node.memory_left
    self.free_memory = free_mem
    return free_mem