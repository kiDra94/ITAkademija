import time

def tick(fps):
    pass

last_tick = 0
target_fps = 1000 / 60
current_frame = 0
last_sec = 0

while True:
    instant = time.time()  
    now = instant * 1000
    time_diff = now - last_tick

    if time_diff >= target_fps:
        tick(current_frame)
        current_frame+=1
        last_tick = now

    if instant - last_sec >= 1:
        print(f"\rFps: {current_frame}",end="") 
        current_frame = 0
        last_sec = instant

    time.sleep(0.0001)