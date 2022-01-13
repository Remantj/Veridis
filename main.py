"""
    Fichier permettant de contrôler les capteurs
"""

import time
from grove.gpio import GPIO
from grove.adc import ADC
from python_sql import *
from numpy import mean
from mail import envoi




button = GPIO(12)
Sound_sensor = GPIO(16)
usleep = lambda x: time.sleep(x / 1000000.0)
 
_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

sound_sensor_active = False
grove_ranger_active = False

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
 


def prise_references():
    """
    Fonction permettant la prise des valeurs de référence,
    une fois la fonction lancée, la prise de valeurs sera effectuée lorsque le bouton sera pressé
    """
    liste_son = []
    son_ref = 0
    distance_ref = 0
    button.dir(GPIO.IN)
    while True:
        if button.read() == 1:
            Sound_sensor.dir(GPIO.IN)
            for i in range(25):
                liste_son.append(GroveSoundSensor(int(0)).sound)
                time.sleep(0.2)
            distance_ref = float(GroveUltrasonicRanger(int(6)).get_distance())
            son_ref = float(mean(liste_son))
            reference(distance_ref, son_ref)
            break

def captation():
    """
    Fonction permettant la prise de valeurs via les capteurs
    """
    son_ref = sound_ref()
    distance_ref= range_ref()
    son_actu = 0
    dist_actu = 0
    while True:     
        time.sleep(5)
        if grove_ranger_active:
            dist_actu = float(GroveUltrasonicRanger(int(6)).get_distance())
            if dist_actu < distance_ref:
                ultrasonic_ranger(1, dist_actu)
                envoi()
        if sound_sensor_active:
            son_actu = int(GroveSoundSensor(int(0)).sound)
            if son_actu + 100 > son_ref:
                sound_sensor(son_actu)
                

