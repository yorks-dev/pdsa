import time

start_time = time.perf_counter()

counter = 0
for i in range(1, 100000):
    counter += 189
    counter *= 2

end_time = time.perf_counter()

print(f"Time : {end_time-start_time}")
