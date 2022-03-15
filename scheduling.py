
# CS 430 Programming Project

# Team Members:

# Member:1
# Name: Komal Bodhankar
# CWID: A20492705

# Member:2
# Name: Esha Choudhary
# CWID: A20492811


# importing heapq library to use heap data structure for sorting jobs and machine w.r.t finish time

import heapq

# Below function reads input file, input.txt, as below:
# Line 1: Total number of machines --> m
# Rest of the lines are considered as a list of tuple with (start,finish) for each job --> data
# Displaying the "Total number of machines: m"
# Displaying all jobs "Jobs: data" 


if __name__ == '__main__':
    data=[]
    input = open('input.txt').readlines()
    m = int(input[0])
    input = input[1:]
    for x in input:
        data.append(tuple(map(int, x.split(' '))))
    print('Total number of machines', m)
    print('\nJobs \n', data)


# Here we have considered the value m to build a list of machines.
# We are currently initializing finish time for each machine as 0. 

machines = list(range(m))
finish_time = [0]*len((range(m)))

# We are creating a list of tuples with finish time for each machine with machine value itself

def merge(finish_time,machines):
    queue = [(finish_time[i],machines[i]) for i in range (0, len(finish_time))]
    return queue

# We are storing entire value of function merge, merging of finish time and machine value, in a variable named queue.
# Then we heapify queue, that is it pops the one with earliest_finish time for any machine first.

queue = merge(finish_time,machines)
heapq.heapify(queue)


# Below function is used for finding the optimal schedule for each machine.

def scheduling(data):

    # Initialized optimal list of len(range(m))
    optimal = [[] for _ in range(m)]

    # Initialized not_processed list
    not_processed = []

    # Exit with error if the total number of machines is more than the total number of Jobs.

    if m > len(data): 
        raise ValueError("Total number of Jobs must be greater than total number of machines.")
    
    # If the above condition is not satisfied, \
    # Execute the interval scheduling algorithm as given below for finding optimal solution of each machine.

    else: 
        for s,f in data:

            # If the start time and finish time of current chosen job is same, \
            # then add that job to not_processed queue.

            if s == f:
                not_processed.append((s,f))
                continue    

            # Pop the machine number for which the earliest finish time is least.

            earliest_finish_time, machine_number = heapq.heappop(queue)

            # If the earliest finish time of chosen machine is less than the start time of current job
            # and
            # If the start time of current job is less than the finish time of current job, then enter loop.
            if earliest_finish_time <= s and s<f:  

                # Here we append optimal solution for the chosen machine in optimal list, \
                # as a tuple which holds the start,finish of job.
                optimal[machine_number].append((s,f))

                # Now we update the finish time for the chosen machine with the finish time of the chosen job.
                heapq.heappush(queue, (f, machine_number))
            else:

                # If above conditions are not satisfied, all such pairs are appended in not_processed queue.
                not_processed.append((s,f))
                heapq.heappush(queue, (earliest_finish_time,machine_number))
        
        # Function returns optimal list and not_processed list in the end.
        return optimal, not_processed

# Initially we sort jobs with respect to Finish time.
# data.sort(key=lambda x: x[1])
data.sort(key=lambda x: x[1])

# Then we sort jobs with respect to start time, \
# To ensure more efficiency and provide output with less not_processed jobs.

# data.sort(key=lambda x: x[0])

# Here we are using the values of optimal and not_processed to print the output,\
# In output we are displaying optimal of each machine and total number of jobs that were not processed.
optimal, not_processed = scheduling(data)
for i in range(1,m+1):
    print('\nMachine #%s has jobs: \n' %i, optimal[i-1])
print('\nJobs not processed: \n', not_processed)
print('\nTotal number of Jobs not processed:  \n', len(not_processed))