#!/usr/bin/env python
"""
A module to interface with the Qnap built in LCD, (c) 2014-2022 Bkram
"""
import serial


class QnapDisplay:
    """
    Class to interface with the LCD
    """
    # Qnap connects its serial to ttys1
    ser = serial.Serial('/dev/ttyS1', 1200)

    # 8 bit keycodes from serial controller
    down = [b'S\x05\x00\x02S\x05\x00\x00',
            b'S\x05\x00\x00S\x05\x00\x02',
            b'S\x05\x00\x02S\x05\x00\x00']
    up = [b'S\x05\x00\x01S\x05\x00\x00',
          b'S\x05\x00\x00S\x05\x00\x01',
          b'S\x05\x00\x01S\x05\x00\x00']
    both = [b'S\x05\x00\x01S\x05\x00\x03',
            b'S\x05\x00\x02S\x05\x00\x03',
            b'S\x05\x00\x03S\x05\x00\x00']

    def init(self):
        """
        Initialize the LCD
        """
        self.ser.write(b'M\0')
        initlcd = self.ser.read(4)
        if initlcd != 'S\x01\x00}':
            return False
        return True

    def write(self, row, text):
        """
        Write text to the LCD
        """
        if row == 0:
            initrow = 'M\f\0\20'
        elif row == 1:
            initrow = 'M\f\1\20'
        writerow = '%s%s' % (initrow, text.ljust(16)[:16])
        self.ser.write(b'M^\1')
        self.ser.write(writerow.encode())

    def read(self):
        """
        Read a keypress from the panel
        """
        key = self.ser.read(8)
        if key in self.down:
            state = 'Down'
        elif key in self.up:
            state = 'Up'
        elif key in self.both:
            state = 'Both'
            # Ignore next event as it is always bogus after both keys are
            # pressed.
            self.ser.read(8)
        else:
            print("Unknown key: ", key)
            state = 'unknown'
        return state

    def enable(self):
        """
        Enable LCD backlight
        """
        self.ser.write(b'M^\1\n')

    def disable(self):
        """
       Disable LCD backlight
        """
        self.ser.write(b'M^\0\n')
