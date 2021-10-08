from machine import Pin, Timer
import utime


####### 보드가 기본 동작을 하고 있는지
####### 확인할 수 있도록 LED를 깜빡입니다.
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=20, mode=Timer.PERIODIC, callback=blink)

####### 사운드센서(마이크 입력)을 위한 코드
from machine import Pin, ADC
import utime

# 아래 코드는 사운드 센서에서 아날로그로 입력받는 코드 입니다.
# MIC_PIN = 28 # GP28 == ADC2
# mic_adc = ADC(MIC_PIN)
# while True:
# reading = mic_adc.read_u16()    
# print("MIC: ",reading)
# utime.sleep(0.2)

####### 디지털로 사운드 센서 입력을 받기 위해 설정합니다.
####### 가져온 값이 0이면 기준보다 큰 소리가 발생한 상태이며,
####### 가져온 값이 1이면 기준보다 작은 소리 입니다.
MIC_PIN = 28
mic = Pin(MIC_PIN, Pin.IN)

# PWM으로 진동 모듈을 제어하는 코드 입니다.
import utime
from machine import Pin, PWM

# 진동 강도를 설정하는 함수 입니다.
# vib_strength(1)이면 약한 강도이고,
# vib_strength(3)이면 가장 강도 입니다.
def vib_strength(level):
    level_values = [0, 45536, 55536, 65536]
    pwm.duty_u16(level_values[level])

# 진동 모듈은 26번 핀에 연결합니다.
pwm = PWM(Pin(26))
pwm.freq(1000)

##################################
##################################
while True: ####### 계속 루프를 돕니다.
     reading = mic.value()
     print(reading)####### 마이크 센서에서 값을 가져옵니다.
     if (reading == 0) :
        ##### 최고 강도로 진동합니다.
        vib_strength(3)
        print("Vibration!")
        ##### 1초 동안 진동합니다.
        utime.sleep(1)
        vib_strength(0)
     else:
        utime.sleep(0.2)