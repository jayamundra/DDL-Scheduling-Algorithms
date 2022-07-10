from enum import Enum

class Status(Enum):
    READY = 0
    PENDING = 1     # in queue
    RUNNING = 2
    PREEMPT = 3
    END = 4

class Job:
    def __init__(self, job_id, start_time, end_time, submission_time, user, num_gpu):
        self.jobID = job_id
        self.traceStartTime = start_time
        self.traceEndTime = end_time
        self.arrivalTime = submission_time
        self.userId = user
        self.numGPU = num_gpu

        self.jobStatus = Status.READY
        self.startTime = -1
        self.endTime = -1
        self.totalExecutionTime = 0
        self.pendingTime = 0
        self.jobPriority = -1