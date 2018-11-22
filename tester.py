from schedule import Schedule
from user import User
import time
import datetime

def main():
    miguel = User('Miguel', Schedule())
    print(time.asctime(time.localtime(time.time())))


if __name__ == "__main__":
    main()                                                        