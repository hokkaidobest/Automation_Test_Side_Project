# Week 1 Part 1

## Assignment 1: Multi-thread (Python) 

Today, we want to finish some jobs in multi-thread and you can see the sample code below.  The main function executes the do_job function 5 times and in each time it takes 3 seconds to  finish the job. So it will take 15 seconds to finish all the jobs and that is very inefficient. We  want to finish all the jobs in around 3 seconds in total, try to rewrite the main function to  achieve the goal and keep other functions untouched. 

```python
import threading 
from time import sleep 

def do_job(number): 
   sleep(3) 
   print(f"Job {number} finished") 

# rewrite everything inside this main function and keep others untouched 
def main(): 
   for i in range(5): 
       do_job(i) 

main()
```


Reminder:  
1. You don’t need to take care about the order of job execution, just make sure all jobs are  executed and finished.
