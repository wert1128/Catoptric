import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motorkit import stepper as STEPPER

def turnOffMotors():
    kit.stepper1.release()
    kit.stepper2.release()

kit = MotorKit(i2c=board.I2C())

for i in range(100):
    kit.stepper1.onestep(direction=STEPPER.BACKWARD)
    time.sleep(0.01)

for i in range(100):
    kit.stepper1.onestep(direction=STEPPER.FORWARD)
    time.sleep(0.01)

for i in range(100):
    kit.stepper2.onestep(direction=STEPPER.BACKWARD)
    time.sleep(0.01)

for i in range(100):
    kit.stepper2.onestep(direction=STEPPER.FORWARD)
    time.sleep(0.01)

turnOffMotors()