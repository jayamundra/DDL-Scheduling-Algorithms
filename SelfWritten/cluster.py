from switch import *

class Cluster:
  def __init__(self, id, switch_count, node_p_switch, cpu_p_node, gpu_p_node, memory_p_node):
    self.id = id
    self.switch_count = id
    self.total_nodes = switch_count * node_p_switch
    self.cpu_count = self.total_nodes * cpu_p_node
    self.gpu_count = self.total_nodes * gpu_p_node
    self.total_memory = self.total_nodes * memory_p_node
    self.switch_list = dict()
    
    # creating cluster
    for i in range(switch_count):
      self.switch_list[i] = Switch(i, node_p_switch, cpu_p_node, gpu_p_node, memory_p_node)
      
      
  def free_gpu_count(self):
    count = 0
    for _, sw in self.switch_list.items():
      count += sw.free_gpu_count()
    return count
  
  def calc_free_memory(self):
    free_memory = 0
    for sw in self.switch_list.values():
      free_memory += sw.calc_free_memory()
    return free_memory
  
  def placement(self, gpu_req, mem_req, how='yarn'):
    if self.free_gpu_count() < gpu_req or self.calc_free_memory() < mem_req:
      print("Cluster does not possess enough free GPUs or free memory")
      return None
    
    # YARN
    if how.lower() == 'yarn':
      for sw in self.switch_list.values():
        if sw.free_gpu_count() >= gpu_req and sw.calc_free_memory() >= mem_req:
          print(f"Job placement possible on switch with index {sw.id}")
          return sw.id
        
      print("No Switch has free GPUs or memory required")
      return None