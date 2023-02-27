import wiringpi as piwiring
import time
pin2 = 17

piwiring.wiringPiSetup()
piwiring.pinMode(pin2, 1)
piwiring.softPwmCreate(pin2, 1000, 2000)



delay = 5
while True:
    piwiring.softPwmWrite(pin2, 1000)
    time.sleep(delay)
    piwiring.softPwmWrite(pin2, 1500)
    time.sleep(delay)
    piwiring.softPwmWrite(pin2, 2000)
    time.sleep(delay)
