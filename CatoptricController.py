from adafruit_motorkit import MotorKit
import board
import sys
import time
from adafruit_motor import stepper as STEPPER
import csv

class CatoptricController():
    HELPER_MESSAGE = 'helper_message, tbd'
    def __init__(self):
        self.kit = MotorKit(i2c=board.I2C())

    def parse_and_run(self, argv):
        if len(argv) < 2:
            print("no action argument was given")
            return
        if argv[1] == "quit" or argv[1] == "q":
            self.cleanup()
            print("successfully shut down")
            return
        if argv[1] == "test":
            print("running test")
            self.test()
            return
        if argv[1] == "run_csv":
            if not argv[2]:
                print("please enter the name of the csv file to run")
            elif self.run_csv(argv[2]):
                print("csv ran successfully")
            else:
                print("csv not found")
            return
        if argv[1] == "move":
            if len(argv) != 5:
                print("Enter the correct arguments: move $motor $direction $steps")
                return
            if self.move(int(argv[2]), int(argv[3]), int(argv[4])):
                print("moved successfully")
            else:
                print("move failed")
            return
        print(self.HELPER_MESSAGE)
    
    def run_csv(self, filename):
        try:
            with open('csv/'+filename, newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                for row in csv_reader:
                    _, motor, direction, steps = row
                    self.move(int(motor), int(direction), int(steps))
            self.cleanup()
        except Exception:
            return False    
        return True

    def move(self, motor, direction, steps):
        if motor == 1:
            stepper = self.kit.stepper1
        elif motor == 2:
            stepper = self.kit.stepper2
        else:
            return False
        if direction:
            stepper_dir = STEPPER.FORWARD
        else:
            stepper_dir = STEPPER.BACKWARD

        for _ in range(steps):
            stepper.onestep(direction=stepper_dir)
        return True
        
    def cleanup(self):
        self.kit.stepper1.release()
        self.kit.stepper2.release()
    
    def test(self):
        for _ in range(100):
            self.kit.stepper1.onestep(direction=STEPPER.BACKWARD)
            time.sleep(0.01)

        for _ in range(100):
            self.kit.stepper1.onestep(direction=STEPPER.FORWARD)
            time.sleep(0.01)

        for _ in range(100):
            self.kit.stepper2.onestep(direction=STEPPER.BACKWARD)
            time.sleep(0.01)

        for _ in range(100):
            self.kit.stepper2.onestep(direction=STEPPER.FORWARD)
            time.sleep(0.01)
        self.cleanup()

if __name__ == "__main__":
    main_controller = CatoptricController()
    main_controller.parse_and_run(sys.argv)