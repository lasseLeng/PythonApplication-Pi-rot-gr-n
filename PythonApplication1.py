import RPi.GPIO as GPIO
from datetime import datetime
import time

# GPIO-Setup
GPIO.setmode(GPIO.BCM)
RED_LED = 18
GREEN_LED = 23
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

try:
    while True:
        # Aktuelle Uhrzeit abrufen
        now = datetime.now()
        current_hour = now.hour

        # LED-Logik: 20:00 bis 7:00 -> rote LED, sonst grüne LED
        if 20 <= current_hour or current_hour < 7:
            GPIO.output(RED_LED, GPIO.HIGH)    # Rote LED an
            GPIO.output(GREEN_LED, GPIO.LOW)   # Grüne LED aus
        else:
            GPIO.output(RED_LED, GPIO.LOW)     # Rote LED aus
            GPIO.output(GREEN_LED, GPIO.HIGH)  # Grüne LED an

        # Einmal pro Minute prüfen
        time.sleep(60)

except KeyboardInterrupt:
    # GPIO sauber zurücksetzen, falls Programm abgebrochen wird
    GPIO.cleanup()

