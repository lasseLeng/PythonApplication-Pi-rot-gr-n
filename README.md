# Raspberry Pi LED Steuerung: Rote und Grüne LED basierend auf Uhrzeit

Dieses Projekt verwendet einen Raspberry Pi, um zwei LEDs (eine rote und eine grüne) zu steuern. Die LEDs leuchten je nach Uhrzeit:
- Zwischen **20:00 und 7:00 Uhr** leuchtet die **rote LED**.
- Ansonsten leuchtet die **grüne LED**.

## Materialien
1. Raspberry Pi (alle Modelle geeignet)
2. Rote LED
3. Grüne LED
4. Zwei 220-Ohm-Widerstände
5. Steckbrett und Jumperkabel

## Verkabelung
1. **Rote LED**:
   - Verbinde das längere Bein (Anode) der roten LED über einen 220-Ohm-Widerstand mit einem GPIO-Pin (z.B. GPIO 18).
   - Verbinde das kürzere Bein (Kathode) der LED mit einem GND-Pin des Raspberry Pi.

2. **Grüne LED**:
   - Verbinde das längere Bein (Anode) der grünen LED über einen weiteren 220-Ohm-Widerstand mit einem anderen GPIO-Pin (z.B. GPIO 23).
   - Verbinde das kürzere Bein (Kathode) der LED ebenfalls mit einem GND-Pin des Raspberry Pi.

## Installation der benötigten Bibliothek
Falls die `RPi.GPIO`-Bibliothek noch nicht installiert ist, kannst du sie mit folgendem Befehl installieren:

```bash
pip install RPi.GPIO
```

## Pyhton Code:
```bash
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

