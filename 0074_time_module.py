import time
from time import process_time as my_timer
import random

# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())

# time_here = time.localtime()
# print(time_here)
# print('Year:', time_here[0], time_here.tm_year)
# print('Day:', time_here[1], time_here.tm_mon)
# print('Day:', time_here[2], time_here.tm_mday)

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} second".format(end_time - start_time))