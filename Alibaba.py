import argparse

# receives an Alibaba file and return a vector of Task

class Task:
     def _init_(self, identifier: int, resource: float, walltime: int, submissionTime: int, jobId: int, dependencies, dependents):
          self.id = identifier
          self.resource: int = resource
          self.walltime: int = walltime
          self.submissionTime: int = submissionTime
          self.jobId: int = jobId
          self.allocatedAt: int = None
          self.startTime: int = None
          self.dependencies: list[int] = dependencies
          self.dependents: list[int] = dependents

def name(self, job_name):
     return [int(x) for x in job_name[1][:1].split("_")][0]

def create_objects(self, filename):
     jobs = []
     with open(filename, 'r', encoding='utf8') as f:
          for line in f.readlines(): 
               jobs.append(line.split())

     def dependencies(self, job_name) -> list[int]:
          return [int(x) for x in job_name.split("_")[:1]]  # M1_3_4 -> [3,4]    

     def dependents(self, job_name, all_jobs) -> list[int]:
          dependencies = []

          for job in all_jobs:  # job list
               for dependency in job.dependencies(job[1]):  # for each dependency in the dependencies list of each job
                    if dependency == [int(x) for x in job_name[:1].split("_")][0]:  # if any dependency == this job's name
                         dependencies.append([int(x) for x in job_name[:1].split("_")][0])  # dependencies.append(jobs name without depedency)

          return dependencies

     tasks = []
     for job in jobs:
          tasks.append( Task(job[0], job[11], job[6] - job[5], job[5], name(job), dependencies(job[1]), dependents(job[1], jobs)) )
     
     return tasks

if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('file_name', help='Input file')
     arg = parser.parse_args()

     print(create_objects(arg.file_name))

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