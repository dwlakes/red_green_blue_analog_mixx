import RPi.GPIO as GPIO
import ADC0384
from time import sleep

LEDpin16 = 16
LEDpin20 = 20
LEDpin21 = 21

GPIO.setmode(GPIO.BCM)
ADC0384.setup()

GPIO.setup(LEDpin16, GPIO.OUT)
GPIO.setup(LEDpin20, GPIO.OUT)
GPIO.setup(LEDpin21, GPIO.OUT)

myPWMRed = GPIO.PWM(LEDpin16, 100)
myPWMGreen = GPIO.PWM(LEDpin20, 100)
myPWMBlue = GPIO.PWM(LEDpin21, 100)

try:
    while True:
        analogVal0 = ADC0384.getResult(0)
        analogVal1 = ADC0384.getResult(1)
        analogVal2 = ADC0384.getResult(2)
        
        dutyCycleRed = analogVal0/2.555
        dutyCycleGreen = analogVal1/2.555
        dutyCycleBlue = analogVal2/2.555

        # Red analog
        if analogVal0 > 0:
            myPWMRed.start(dutyCycleRed)
            myPWMRed.ChangeDutyCycle(dutyCycleRed)  
        else: 
            GPIO.output(LEDpin16, False)
            myPWMRed.stop()

        # Green analog
        if analogVal1 > 0:
            myPWMGreen.start(dutyCycleGreen)
            myPWMGreen.ChangeDutyCycle(dutyCycleGreen)  
        else: 
            GPIO.output(LEDpin20, False)
            myPWMGreen.stop()

        # Blue analog
        # Red analog
        if analogVal2 > 0:
            myPWMBlue.start(dutyCycleBlue)
            myPWMBlue.ChangeDutyCycle(dutyCycleBlue)  
        else: 
            GPIO.output(LEDpin21, False)
            myPWMBlue.stop()

        print("Analog 0: ",analogVal0)
        print("DCRed: ", dutyCycleRed)
        print("\n")
        print("Analog 1: ",analogVal1)
        print("DCGreen: ", dutyCycleGreen)
        print("\n")
        print("Analog 2: ",analogVal2)
        print("DCBlue: ", dutyCycleBlue)
        sleep(.2)


except KeyboardInterrupt:
    GPIO.cleanup()
    print("adios")
