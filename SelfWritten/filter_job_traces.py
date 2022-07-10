import json

def filter_job_traces():
    f = open("trace-data/cluster_job_log")
    data = json.load(f)

    filtered_traces = [x for x in data if x['status'] == 'Pass' and len(x['attempts']) == 1]

    json_string = []
    for d in filtered_traces:
        #print(d)
        print("attempts!", d['attempts'][0])
        trace = {
            "jobid": d['jobid'],
            "start_time": d['attempts'][0]['start_time'],
            "end_time": d['attempts'][0]['end_time'],
            "submitted_time": d['submitted_time'],
            "user": d['user']
        }
        gpus = []
        for req in d['attempts'][0]['detail']:
            gpus += req['gpus']
            #gpus.concat(req['gpus'])
        trace['gpus'] = gpus
        json_string.append(trace)
    
    with open('filtered_traces/cluster_job_log', 'w') as outfile:
        json.dump(json_string, outfile)

filter_job_traces()
