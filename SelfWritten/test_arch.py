from cluster import *

def main():
  cluster1 = Cluster(0, 4, 2, 2, 2, 100)
  print(cluster1.free_gpu_count())
  print(cluster1.placement(4, 200, 'yarn'))
  
if __name__ == "__main__":
  main()