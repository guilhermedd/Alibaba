import argparse
import csv

# receives an Alibaba file and return a vector of Task

class Task:
     def __init__(self, identifier: int, resource: float, walltime: int, submissionTime: int, jobId: int, dependencies, dependents):
          self.id = identifier
          self.resource: int = resource
          self.walltime: int = walltime
          self.submissionTime: int = submissionTime
          self.jobId: int = jobId
          self.allocatedAt: int = None
          self.startTime: int = None
          self.dependencies: list[int] = dependencies
          self.dependents: list[int] = dependents

     def __repr__(self):
          return f'Id: {self.id}, Resource: {self.resource}, Walltime: {self.walltime}, Submition Time: {self.submissionTime}, Job Id: {self.jobId}, Alocated At: {self.allocatedAt}, Start Time: {self.startTime}, Dependencies: {self.dependencies}, Dependents: {self.dependents}'  

def name(job_name):
     return [int(x) for x in job_name[1:].split("_")][0]  # M10_3_4 -> 10

def dependencies(job_name) -> list[int]:
     return [int(x) for x in job_name.split("_")[1:]]  # M1_3_4 -> [3,4]    

def dependents(job_name, all_jobs) -> list[int]:
     dependen = []

     for job in all_jobs:  # job list
          for dependency in dependencies(job[1]):  # for each dependency in the dependencies list of each job
               if dependency == name(job_name):  # if any dependency == this job's name
                    dependen.append(name(job_name))  # dependencies.append(jobs name without depedency)

     return dependen

def create_objects(filename):
     jobs = []
     with open(arg.file_name, newline='') as f:
          spamreader = csv.reader(f, delimiter=' ', quotechar='|')
          for line in spamreader: 
               # print(line[0])
               jobs.append(line[0].split(','))
     del jobs[0]
     tasks = []
     for job in jobs:
          tasks.append( Task([int(x) for x in job[0].split('_')[1:]][0], int(job[11]), int(job[6]) - int(job[5]), int(job[5]), name(job[1]), dependencies(job[1]), dependents(job[2], jobs)) )  # TODO: make job[0] become a integer

     # for t in tasks:
     #      print(tasks)
     return tasks


if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('file_name', help='Input file')
     arg = parser.parse_args()

     for task in create_objects(arg.file_name): 
          print(task)

# identifier        = [0]          -- instance name
# resource          = [11]         -- max cpu used 
# walltime          = [6] - [5]    -- end - beginning
# submissionTime    = [5]          -- start_time
# jobId             = [1]          -- task name
# dependencies      = []           -- depends on which tasks
# dependents        = []           -- which tasks depend on this task

#   0      | instance_name   | string     |       | instance name of the instance                          |  
#   1      | task_name       | string     |       | name of task to which the instance belong              |
#   2      | job_name        | string     |       | name of job to which the instance belong               |
#   3      | task_type       | string     |       | task type                                              |
#   4      | status          | string     |       | instance status                                        |
#   5      | start_time      | bigint     |       | start time of the instance                             |
#   6      | end_time        | bigint     |       | end time of the instance                               |
#   7      | machine_id      | string     |       | uid of host machine of the instance                    |
#   8      | seq_no          | bigint     |       | sequence number of this instance                       |
#   9      | total_seq_no    | bigint     |       | total sequence number of this instance                 |
#   10     | cpu_avg         | double     |       | average cpu used by the instance, 100 is 1 core        |
#   11     | cpu_max         | double     |       | max cpu used by the instance, 100 is 1 core            |
#   12     | mem_avg         | double     |       | average memory used by the instance (normalized)       |
#   13     | mem_max         | double     |       | max memory used by the instance (normalized, [0, 100]) |
