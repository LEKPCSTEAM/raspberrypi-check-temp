import time

def get_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = int(f.read()) / 1000
    return temp

try:
    while True:
        temp = get_temp()
        print(f"🌡️ CPU Temperature: {temp:.2f}°C")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopped monitoring temperature.")
