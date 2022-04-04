from adafruit_motorkit import MotorKit
import board
import sys
import time
from adafruit_motorkit import stepper as STEPPER



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
        if argv[1] == "reset":
            self.reset()
            print("reset successfully")
            return
        if argv[1] == "run":
            if not argv[2]:
                print("please enter the name of the csv file to run")
            elif self.run_csv(argv[2]):
                print("csv ran successfully")
            else:
                print("csv not found")
            return
        print(self.HELPER_MESSAGE)
    
    def run_csv(self, filename):
        return True

    def reset(self):
        return

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