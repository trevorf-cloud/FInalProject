import machine
import sys
import time
import select

led = machine.Pin(21, machine.Pin.OUT)
button = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

while True:
    # Check for serial commands
    if poll.poll(0):
        cmd = sys.stdin.readline().strip()
        if cmd == "ON":
            led.value(1)
        elif cmd == "OFF":
            led.value(0)

    # Check for button
    if button.value() == 0:
        time.sleep(0.05) # Debounce
        if button.value() == 0:
            print("DONE")
            led.value(0)
            while button.value() == 0: # Wait for release
                time.sleep(0.1)
    
    time.sleep(0.1)