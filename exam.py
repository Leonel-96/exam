import time
import datetime 
import threading

stop_thread = False
global_fifo =[]
global_lifo =[]

class my_task(threading.Thread):
    name =None
    period = -1
    execution_time = -1
    last_execution_time = None

    def __init__(self,period,execution_time,last_execution,fifo_write=False,lifo_write=False):
        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.last_execution_time = last_execution
        self.fifo_write = fifo_write
        self.lifo_write = lifo_write

        threading.Thread.__init__(self)

    def run(self):
        self.last_execution_time = datetime.datetime.now()
        global global_fifo
        global global_lifo

        while(not stop_thread):
            print("\t"+self.name+ ":starting pump("+self.last_execution_time.strftime("%H:%M:%S")+ ")")
            if(self.fifo_write == True):
                global_fifo.append(self.name + ":reading message:" + self.last_execution_time.strftime("%H:%M:%S"))
            else:
                while(len(global_fifo) > 0 ):
                    print(self.name+ ":" + global_fifo[0])
                    del global_fifo[0]

            time.sleep(self.execution_time)
            print("\t"+self.name+ ":ending pump("+self.last_execution_time.strftime("%H:%M:%S")+ ")")
            time.sleep(self.period - self.execution_time)


if __name__ == '__main__':

    last_execution = datetime.datetime.now()

    task_list =[]

    task_list.append(my_task(name="pump_1", period=5, execution_time=2,last_execution=last_execution,fifo_write=True))
    task_list.append(my_task(name="pump_2", period=15, execution_time=3,last_execution=last_execution,fifo_write=True))
    task_list.append(my_task(name="machine_1", period=5, execution_time=5,last_execution=last_execution))
    task_list.append(my_task(name="machine_2", period=5, execution_time=3,last_execution=last_execution))

    while(1):
        time_now = datetime.datetime.now()

        print("\nScheduler tick :" + time_now.strftime("%H:%M:%S"))

        task_to_run = None
        earliest_deadline = time_now + datetime.timedelta(hours=1)

        for current_task in task_list:
            current_task_next_deadline = current_task.last_execution_time +datetime.timedelta(seconds=current_task.period)

            print("\tDeadline for task " + current_task.name + " : " + current_task_next_deadline.strftime("%H:%M:%S"))
                    
            if (current_task_next_deadline < earliest_deadline):
                earliest_deadline = current_task_next_deadline
                task_to_run = current_task
        

        task_to_run.run()

            

