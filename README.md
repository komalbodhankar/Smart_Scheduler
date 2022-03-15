# Smart_Scheduler

## Algorithm Design is based on Greedy Algorithm - Interval Scheduling

* In this we will consider jobs in some order and assign jobs in such a manner that it is compaRble with the ones that are already allocated i.e., they do not overlap
* We sort the jobs on the based on:
    * Earliest Finish Time We consider jobs ascending order of finish time
* We are using heap queue in our algorithm which is a way of implemenRng priority queue for prioritizing machines based on their earliest finish time in the most efficient manner


## Input File

* Line 1: Total number of machines --> m
* Lines n-1: List of tuple with (start, finish) for each job --> data

## HeapQ usage

* Maintain a list of tuples with (machine number, finish time) 
> _Note: The value of machine number is chosen from the index value of the Array in which it is stored_
* Utilizing the data - (start, finish) entry from input.txt file, we sort the data set

## Working of the 'Smart_Scheduler'
* We call the greedy algorithm named 'schedule' which finds optimal solution for each machine
* In schedule we have two empty arrays named:
    * optimal[] - Jobs which are eligible to work on any of the machines
    * Not_processed[] - Jobs which weren't compatible with any of the machines
> _Note: Length of optimal[] must be equal to the length of queue, that is, it should be equal to total number of machines, m_
* For each iteration we ensure if below condition is satisfied
    * Total number of machines must be less than total number of jobs, i.e., m<data

## Not-Processed queue cases
_Case 1:_ When start time is equal to finish time of a given job
_Case 2:_ If finish time is greater than start time and earliest finish time of all machines is greater than start time

## Optimal queue cases
_Case 1:_ Start time of a given job should be less than the finish time of the same job
_Case 2:_ Earliest finish time of the machine should be less than or equal to the start time of current job 

## Output - In tuples
By the end of our algorithm, we return the optimal solution for each machine and total number of non-processed jobs in the form of tuples

## Pseudo Code
m _<- Read first line from input.txt_

data {} _<- Create a list of tuples which has start and finish ,mes for each job_

queue {} _<- Contains finish ,me with respect to each machine number_

Sort data/jobs by finish time and then by start time _<- Here we are considering both to ensure that maximum jobs are assigned to all the machines_

optimal [] _<- Initialized an empty array of length m_

non_processed [] _<- Initialized an empty array to append all the not processed jobs_

Def schedule(data):

For start & finish in data: _<- For each job we compare start and finish time for all the conditions_

If (m, machines, is greater than length of data): _<- Problem statement handled_
    * Fail the code by returning an exception

Else:

If (start Rme == finish time):

non_processed [] _<- Append not processed jobs to the list_

Pop the first value from heap queue _<- This provides the machine number with minimum finish time_ 

If (start time < finish time && finish time of the machine <= start time of current job):

optimal [machine] _<- Append the job slot to the list_

Push finish time of chosen job to the heap queue and sort w.r.t finish time.

Else:

None of the conditions are saRsfied by the jobs, hence add them to not processed.

not_processed _<- Append the not processed jobs to the list_

return (optimal, non_processed)

By looping over we print optimal and non-processed jobs for each machine

## Program execution

Run this file using below command:

    >$ python scheduling.py


> _Note: This project uses python3.7_
