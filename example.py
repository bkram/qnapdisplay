#!/usr/bin/env python3
"""
Qnapdisplay example
"""
import time

from qnapdisplay import QnapDisplay


def main():
    """
    Qnapdisplay example
    """
    lcd = QnapDisplay()

    if lcd.init():
        lcd.write(0, 'Qnap Display')
        lcd.write(1, 'Press a key')

        read = lcd.read()
        lcd.write(1, '%s pressed' % (read))
        time.sleep(2)

        lcd.write(0, 'On and Off')
        lcd.write(1, '10 times')

        for incr in range(0, 10):
            print("Loop # {}".format(incr))
            lcd.disable()
            time.sleep(4)
            lcd.enable()
            time.sleep(4)

        lcd.enable()
        lcd.write(0, 'Stay a while')
        lcd.write(1, 'Stay forever')
    else:
        print('Oops something went wrong here')


if __name__ == "__main__":
    main()
