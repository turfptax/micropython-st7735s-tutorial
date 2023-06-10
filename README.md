# micropython-st7735s-tutorial
Tutorial to get ESP32-S2 mini to talk to a TFT ST7735S screen

## Download Micropython Drivers/Files

Goto: https://github.com/boochow/MicroPython-ST7735

Download the following files:
ST7735.py
sysfont.py
graphicstest.py

## Get default SPI(1) pins from ESP32-S2

run the following to find the SCK and SDA(MISO) pins from default values on ESP32-S2:

```python
import machine
print(machine.SPI(1))
```
The output should look like this:

>>> 
