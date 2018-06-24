# OnAir
Code for working an on air light for a raspberry pi

This project is for getting Raspberry Pi to monitor a broadcast url and turn on a light when it detects that the broadcast is on.
This project is based off of one from AdaFruit (https://learn.adafruit.com/internet-streaming-on-air-sign/overview)

To build this project you'll need the following:
1. https://www.raspberrypi.org/products/
2. https://www.amazon.com/POWERSWITCHTAIL-COM-PowerSwitch-Tail-II/dp/B00B888VHM/ref=sr_1_1?ie=UTF8&qid=1529877760&sr=8-1&keywords=power+switch+tail
3. https://www.amazon.com/Westek-AL301B-Outdoor-Voltage-Address/dp/B000HJ98BG/ref=sr_1_7?ie=UTF8&qid=1529877795&sr=8-7&keywords=house+number+light

The power switch tail needs to be setup on on GPIO pin 24 on the PI. (https://pinout.xyz/#)

The current implementation is checking a stream hosted by BoxCast but feel free to fork this project and add additional streaming providers.
