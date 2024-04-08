# Bibliotheken laden
from machine import Pin
from time import sleep

def init_debug_led():
    global led_onboard
    # Initialisierung von GPIO25 als Ausgang
    led_onboard = Pin(25, Pin.OUT)

def on_off_led():
    init_debug_led()
    led_onboard.on()
    sleep(0.2)
    led_onboard.off()
    sleep(0.2)
    led_onboard.on()

def main():
    init_debug_led()
    on_off_led()

if __name__ == "__main__":

    print("___Start_Program___")
    main()      # Start Main $$$
    sleep(2)
    led_onboard.off()
    print("___End_after_Main___!!!")

# Normal sollte das Programm hier nie ankommen !
print("___End_of_Programm___!!!")

# ##############################################################################
