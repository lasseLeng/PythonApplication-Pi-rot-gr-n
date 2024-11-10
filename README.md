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
