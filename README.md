# Micropython ST7735S Tutorial

This repository provides a tutorial to help you get an ESP32-S2 mini to communicate with a TFT ST7735S screen using MicroPython.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Downloading the Required Drivers and Files](#downloading-the-required-drivers-and-files)
- [Identifying the Default SPI Pins](#identifying-the-default-spi-pins)
- [Wiring](#wiring)
- [License](#license)

## Prerequisites

Before you start, ensure you have the following:
- ESP32-S2 mini
- TFT ST7735S screen
- MicroPython firmware installed on your ESP32-S2 mini

## Downloading the Required Drivers and Files

The following drivers and files are required for this tutorial:

### From the MicroPython ST7735 repository:

1. `ST7735.py`
2. `graphicstest.py`

Visit the [MicroPython ST7735 Repository](https://github.com/boochow/MicroPython-ST7735) to download these files.

### From the GuyCarver MicroPython repository:

1. `sysfont.py`

Visit the [GuyCarver MicroPython Repository](https://github.com/GuyCarver/MicroPython/tree/master/lib) to download this file.

## Identifying the Default SPI Pins

Run the following command in the MicroPython REPL to find the SCK (Serial Clock) and SDA (Serial Data) MISO (Master In Slave Out) pins from the default values on ESP32-S2:

```python
import machine
print(machine.SPI(1))
```

The output should look similar to this:
SPI(id=1, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=0, sck=7, mosi=11, miso=9)

## Wiring

Here is a guide on how to wire your ESP32-S2 mini with the TFT ST7735S screen:

![ESP32-S2 to TFT ST7735S Wiring Diagram](https://github.com/turfptax/micropython-st7735s-tutorial/raw/main/images/ESP32s2-Wiring-ST7735S.jpg)


## License
This project is licensed under the terms of the MIT license. For more information, refer to the LICENSE file.
