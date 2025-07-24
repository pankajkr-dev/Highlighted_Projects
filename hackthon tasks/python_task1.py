import android
import time

# Initialize Android interface
droid = android.Android()

# Phone number to call
family_number = "+911234567890"

def get_battery_level():
    battery = droid.batteryGetLevel().result
    return battery

def auto_call_on_low_battery(threshold=5):
    while True:
        battery_level = get_battery_level()
        print(f"Battery level: {battery_level}%")
        if battery_level is not None and battery_level <= threshold:
            print("Battery low! Calling family...")
            droid.phoneCall(family_number)
            break
        time.sleep(60)  # Check every 60 seconds

auto_call_on_low_battery()
