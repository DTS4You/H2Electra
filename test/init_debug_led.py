# Bibliotheken laden
from machine import Pin
from time import sleep

def init_debug_led():
    global led_onboard
    # Initialisierung von GPIO25 als Ausgang
    led_onboard = Pin(25, Pin.OUT)


def main():
    while(1):
        # LED einschalten
        led_onboard.on()
        sleep(0.5)
        # LED ausschalten
        led_onboard.off()
        sleep(0.5)


if __name__ == "__main__":

    print("___Start_Program___")

    init_debug_led()

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End_of_Programm___!!!")

# ##############################################################################
