from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math

def tftprinttest():
    tft.fill(TFT.BLACK);
    v = 30
    tft.text((0, v), "Hello World!", TFT.RED, sysfont, 1, nowrap=True)
    v += sysfont["Height"]
    tft.text((0, v), "Hello World!", TFT.YELLOW, sysfont, 2, nowrap=True)
    v += sysfont["Height"] * 2
    tft.text((0, v), "Hello World!", TFT.GREEN, sysfont, 3, nowrap=True)
    v += sysfont["Height"] * 3
    tft.text((0, v), str(1234.567), TFT.BLUE, sysfont, 4, nowrap=True)
    time.sleep_ms(1500)
    tft.fill(TFT.BLACK);
    v = 0
    tft.text((0, v), "Hello World!", TFT.RED, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), str(math.pi), TFT.GREEN, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " Want pi?", TFT.GREEN, sysfont)
    v += sysfont["Height"] * 2
    tft.text((0, v), hex(8675309), TFT.GREEN, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " Print HEX!", TFT.GREEN, sysfont)
    v += sysfont["Height"] * 2
    tft.text((0, v), "Sketch has been", TFT.WHITE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), "running for: ", TFT.WHITE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), str(time.ticks_ms() / 1000), TFT.PURPLE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " seconds.", TFT.WHITE, sysfont)

### User Defined Pins ####

tft_CS = 5
tft_RESET= 9
tft_A0 = 3
#tft_SDA=11
#tft_SCK=7

# SCK, and MOSI pins can be found by running the following:
## import machine
## print(machine.SPI(1))
#>>> SPI(id=1, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=0, sck=7, mosi=11, miso=9)
# Only need to look at sck=x and mosi=x
### End User Defined Pins ###

spi = SPI(1, baudrate=20000000, polarity=0, phase=0,miso=None)
tft=TFT(spi,tft_A0,tft_RESET,tft_CS)
tft.initr()
tft.rgb(True)

tft.fill(TFT.BLACK)
tft.text((0, 0), "nunc bibendum.", TFT.WHITE, sysfont, 1)
time.sleep_ms(1000)

tftprinttest()
time.sleep_ms(4000)

