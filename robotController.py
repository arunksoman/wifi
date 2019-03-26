import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor
rightA = 7
rightB = 8
leftA = 9
leftB = 10

GPIO.setup(rightA, GPIO.OUT)
GPIO.setup(rightB, GPIO.OUT)
GPIO.setup(leftA, GPIO.OUT)
GPIO.setup(leftB, GPIO.OUT)

# Disable movements on startup
GPIO.output(rightA, GPIO.LOW)
GPIO.output(rightB, GPIO.LOW)
GPIO.output(leftA, GPIO.LOW)
GPIO.output(leftB, GPIO.LOW)

# PWM Initialization

rightMotorFwd = GPIO.PWM(rightA, 15)
leftMotorFwd = GPIO.PWM(leftA, 15)
rightMotorRev = GPIO.PWM(rightB, 15)
leftMotorRev = GPIO.PWM(leftB, 15)

rightMotorFwd.start(15)
leftMotorFwd.start(15)
rightMotorRev.start(15)
leftMotorRev.start(15)

def stop():
    rightMotorFwd.ChangeDutyCycle(0)
    rightMotorRev.ChangeDutyCycle(0)
    leftMotorFwd.ChangeDutyCycle(0)
    leftMotorRev.ChangeDutyCycle(0)

def forward():
    rightMotorFwd.ChangeDutyCycle(15)
    rightMotorRev.ChangeDutyCycle(0)
    leftMotorFwd.ChangeDutyCycle(15)
    leftMotorRev.ChangeDutyCycle(0)
    
def reverse():
    rightMotorFwd.ChangeDutyCycle(0)
    rightMotorRev.ChangeDutyCycle(20)
    leftMotorFwd.ChangeDutyCycle(0)
    leftMotorRev.ChangeDutyCycle(20)
    
def turn_left():
    rightMotorFwd.ChangeDutyCycle(12)
    rightMotorRev.ChangeDutyCycle(0)
    leftMotorFwd.ChangeDutyCycle(15)
    leftMotorRev.ChangeDutyCycle(0)
    
def turn_right():
    rightMotorFwd.ChangeDutyCycle(15)
    rightMotorRev.ChangeDutyCycle(0)
    leftMotorFwd.ChangeDutyCycle(12)
    leftMotorRev.ChangeDutyCycle(0)

def spin_left():
    rightMotorFwd.ChangeDutyCycle(0)
    rightMotorRev.ChangeDutyCycle(0)
    leftMotorFwd.ChangeDutyCycle(15)
    leftMotorRev.ChangeDutyCycle(0)
    
def spin_right():
    rightMotorFwd.ChangeDutyCycle(15)
    rightMotorRev.ChangeDutyCycle(0)
    leftMotorFwd.ChangeDutyCycle(0)
    leftMotorRev.ChangeDutyCycle(0)
    
def back_left():
    rightMotorFwd.ChangeDutyCycle(0)
    rightMotorRev.ChangeDutyCycle(12)
    leftMotorFwd.ChangeDutyCycle(0)
    leftMotorRev.ChangeDutyCycle(15)
    
def back_right():
    rightMotorFwd.ChangeDutyCycle(0)
    rightMotorRev.ChangeDutyCycle(15)
    leftMotorFwd.ChangeDutyCycle(0)
    leftMotorRev.ChangeDutyCycle(12)    
def main():
    reverse()
    time.sleep(5)
    # print("Stop")
    GPIO.cleanup()

if __name__ == "__main__":   
    main()
