import math
import sys
import time
from grove.gpio import GPIO
from grove.adc import ADC
from python_sql import *
from numpy import mean
from mail import envoi
#from grovepi import *
#GPIO.setup(12, GPIO.IN) #Button

button = GPIO(12)
Sound_sensor = GPIO(16)
usleep = lambda x: time.sleep(x / 1000000.0)
 
_TIMEOUT1 = 1000
_TIMEOUT2 = 10000
 
class GroveUltrasonicRanger(object):
    def __init__(self, pin):
        self.dio =GPIO(5)
 
    def _get_distance(self):
        self.dio.dir(GPIO.OUT)
        self.dio.write(0)
        usleep(2)
        self.dio.write(1)
        usleep(10)
        self.dio.write(0)
 
        self.dio.dir(GPIO.IN)
 
        t0 = time.time()
        count = 0
        while count < _TIMEOUT1:
            if self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT1:
            return None

 
        t1 = time.time()
        count = 0
        while count < _TIMEOUT2:
            if not self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT2:
            return None
 
        t2 = time.time()
 
        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None
 
        distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm
 
        return distance
 
    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist

class GroveSoundSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def sound(self):
        value = self.adc.read(self.channel)
        return value
 
#Grove = GroveSoundSensor
 
#Grove = GroveUltrasonicRanger
 
"""def dist():
 
    sonar = GroveUltrasonicRanger(int(6))
 
    print('Detecting distance...')
    while True:
        print('{} cm'.format(sonar.get_distance()))
        time.sleep(1)
 
if __name__ == '__main__':
    dist()

 
 
def sound():
 
    sensor = GroveSoundSensor(int(0))
 
    print('Detecting sound...')
    while True:
        print('Sound value: {0}'.format(sensor.sound))
        time.sleep(.3)"""
 
liste_son = []
son_ref = 0
distance_ref= 0
son_actu = 0
dist_actu = 0
actif = False

while True:     
    button.dir(GPIO.IN)
    if button.read() == 1:
        """if __name__ == '__main__':
            sound()"""
        Sound_sensor.dir(GPIO.IN)
        for i in range(25):
            liste_son.append(GroveSoundSensor(int(0)).sound)
            time.sleep(0.2)
        distance_ref = float(GroveUltrasonicRanger(int(6)).get_distance())
        son_ref = float(mean(liste_son))
        reference(distance_ref, son_ref)
        actif = True
    
    if actif:
        dist_actu = float(GroveUltrasonicRanger(int(6)).get_distance())
        if dist_actu < distance_ref:
            ultrasonic_ranger(1, dist_actu)
            envoi()
        son_actu = int(GroveSoundSensor(int(0)).sound)
        if son_actu + 100 > son_ref:
            sound_sensor(son_actu)
