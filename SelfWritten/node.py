class Node:
  def __init__(self, id, cpu_count, gpu_count, memory):
    self.id = id
    self.cpu_count = cpu_count
    self.gpu_count = gpu_count
    self.total_memory = memory
    self.free_gpus = self.gpu_count
    self.memory_left = self.total_memory
  
