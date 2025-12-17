import time
import usb_hid
import board
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

INTERVAL_MS = 60000
STEP_DELAY_MS = 300     

last_cycle = time.monotonic_ns() // 1_000_000
state = 0  

while True:
    now = time.monotonic_ns() // 1_000_000

    if state == 0 and (now - last_cycle) >= INTERVAL_MS:
        mouse.move(x=1, y=0)
        state = 1
        step_time = now

    elif state == 1 and (now - step_time) >= STEP_DELAY_MS:
        mouse.move(x=-1, y=0)
        last_cycle = now   
        state = 0
