#!/usr/bin/env python3
"""
Qnapdisplay button test
"""
from qnapdisplay import QnapDisplay


def main():
    """
    Qnapdisplay button test
    """
    lcd = QnapDisplay()

    if lcd.init():
        lcd.enable()
        lcd.write(1, '')

        for keypress in range(1, 10):
            lcd.write(0, 'Enter key %d' % keypress)
            read = lcd.read()
            print('%s pressed' % read)
            lcd.write(1, '%s pressed' % read)

        lcd.write(0, '')
        lcd.write(1, '')
        lcd.disable()

    else:
        print('Oops something went wrong here')


if __name__ == "__main__":
    main()
