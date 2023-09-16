import time

def focus_clock(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Time left: {seconds // 60} minutes {seconds % 60} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Good job focusing!")
  
