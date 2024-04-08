# Bibliotheken laden
from machine import Pin
from time import sleep

# Initialisierung von GPIO25 als Ausgang
led_onboard = Pin(25, Pin.OUT)

# LED einschalten
led_onboard.on()

# 5 Sekunden warten
sleep(1)

# LED ausschalten
led_onboard.off()