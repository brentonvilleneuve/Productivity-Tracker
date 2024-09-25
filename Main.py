import time

class Timer:
    def __init__(self,name):
        self.name = name
        self.start_time = 0
        self.final_time = 0

    def start(self):
        self.start_time = time.time_ns
        print("Timer has been started\n")

    def stop(self):
        if self.start_time == 0:
            print("You didn't start a timer yet\n")
        else:
            self.final_time = (time.time_ns-self.start_time)/1000000000
            print("Timer length: ",self.final_time,"seconds\n")


t1 = Timer("First Timer")

instruction = input("Press enter to start timer\n")
print(t1.name)
print(t1.start_time)
print(t1.final_time)

t1.start()

print(t1.name)
print(t1.start_time)
print(t1.final_time)

instruction = input("Press enter to stop timer\n")
print(t1.name)
print(t1.start_time)
print(t1.final_time)

t1.stop()

print(t1.name)
print(t1.start_time)
print(t1.final_time)