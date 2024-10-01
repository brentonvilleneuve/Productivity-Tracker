import time

class Timer:
    def __init__(self,name):
        self.name = name
        self.start_time = 0
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time_ns()
        print("Timer has been started\n")

    def pause(self):
        if self.start_time == 0:
            print("You didn't start a timer yet\n")
        else:
            self.elapsed_time = self.elapsed_time + (time.time_ns() - self.start_time)
        
    def print_final_time(self):
        print("Final timer: {:0.2f}".format(self.elapsed_time / 1000000000),"seconds\n")

    def print_current_time(self):
        print("Current timer: {:0.2f}".format((self.elapsed_time + (time.time_ns() - self.start_time)) / 1000000000),"seconds\n")

    def reset(self):
        self.elapsed_time = 0


t1 = Timer("First Timer")

print("Name of timer: {}\n".format(t1.name))

instruction = input("Press enter to start timer\n")
t1.start()

instruction = input("Press enter to print current timer\n")
t1.print_current_time()

instruction = input("Press enter to stop timer\n")
t1.pause()

instruction = input("Press enter to print final timer\n")
t1.print_final_time()


