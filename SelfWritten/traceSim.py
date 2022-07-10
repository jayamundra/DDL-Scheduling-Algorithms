import json

def jobLocTrace():
    f = open("trace-data/cluster_job_log")
    data = json.load(f)

    jobList = []
    gpuCountList = []

    passes = 0
    killed = 0
    failed = 0
    attempt_count = 0

    for d in data:
        arr = []
        for a in d['attempts']:
            gpuCount = 0
            for detail in a['detail']:
                gpuCount += len(detail['gpus'])
            # print(d['jobid']+" "+a['start_time']+" "+a['end_time']+" "+str(gpuCount))
            # if a['start_time']!= None:
            #     datetime.datetime.strptime(a['start_time'], '%Y-%m-%d %H:%M:%S');
            if gpuCount not in gpuCountList:
                gpuCountList.append(gpuCount)
        if d['status'] == "Pass":
            passes += 1
            if len(d['attempts']) > 1:
                attempt_count += 1
        elif d['status'] == "Killed":
            killed += 1
        elif d['status'] == "Failed":
            failed += 1

    print(sorted(gpuCountList))
    print(len(data))
    print(str(passes) + " " + str(killed) + " "+str(failed))
    print(attempt_count)

def clusterMachineList():
    with open("trace-data/cluster_machine_list") as f:
        lines = f.readlines()

        arrM = {}
        gpuCount = 0
        totalM = 0
        for l in lines[1:]:
            if l.split(",")[0] not in arrM:
                arrM[l.split(",")[0]] = []
            arrM[l.split(",")[0]].append([[int(l.split(",")[1]), int(l.split(",")[2].strip()[:-2])]])
            gpuCount += int(l.split(",")[1])
            totalM += int(l.split(",")[2].strip()[:-2])
        print(len(arrM), gpuCount, totalM)


# jobLocTrace()
clusterMachineList()