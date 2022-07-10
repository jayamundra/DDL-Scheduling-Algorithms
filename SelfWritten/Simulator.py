import sys
import json

from cluster import Cluster
from Job import *

CLUSTER = Cluster()
allJobList = {}
currEvents = []

def createCluster(fileName):
    with open(fileName) as file:
        lines = file.readlines()

        line = lines[1]
        arr = [int(x) for x in line.strip().split(",")]
        num_switch = arr[0]
        num_node_p_switch = arr[1]
        num_gpu_p_node = arr[2]
        num_cpu_p_node = arr[3]
        mem_p_node = arr[4]
        CLUSTER.init(num_switch, num_node_p_switch, num_gpu_p_node, num_cpu_p_node, mem_p_node)

def readTraceFile(fileName):
    f = open(fileName)
    data = json.load(f)
    for d in data:
        j = Job(d['jobid'], d['start_time'], d['end_time'], d['submitted_time'], d['user'], len(d['gpus']))
        allJobList[d['jobid']] = j
        addJobsToEventList(j)

def addJobsToEventList(job):
    index = 0
    while index < len(currEvents):
        if currEvents[index] > job.arrivalTime:
            break
        index += 1

    currEvents.insert(index, job)

def dlas():
    while True:
        if len(currEvents)==0:
            break

        currJ = currEvents.pop(0)
        currTime = currJ.

def dlas_gittins():
    pass

def gandiva():
    pass

def main():
    if len(sys.argv) != 4:
        print("Invalid number of arguments. Run as python Simulator.py <clusterConfig> <traceFile> <SchedulingAlgo>")

    clusterFile = sys.argv[1]
    traceFile = sys.argv[2]
    schedAlgo = sys.argv[3]

    createCluster(clusterFile)
    readTraceFile(traceFile)

    if schedAlgo == "2DLAS":
        dlas()
    elif schedAlgo == "gittins":
        dlas_gittins()
    elif schedAlgo == "gandiva":
        gandiva()
    else:
        print("Invalid Scheduling algorithms!")


if __name__ == '__main__':
    main()