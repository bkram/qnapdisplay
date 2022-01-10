#!/usr/bin/env python
"""
A module to interface with the Qnap built in LCD, (c) 2014-2022 Bkram
"""
import serial


class QnapDisplay:
    """
    Class to interface with the LCD
    """
    # 8 bit keycodes from serial controller
    __down = [b'S\x05\x00\x02S\x05\x00\x00',
              b'S\x05\x00\x00S\x05\x00\x02',
              b'S\x05\x00\x02S\x05\x00\x00']
    __up = [b'S\x05\x00\x01S\x05\x00\x00',
            b'S\x05\x00\x00S\x05\x00\x01',
            b'S\x05\x00\x01S\x05\x00\x00']
    __both = [b'S\x05\x00\x01S\x05\x00\x03',
              b'S\x05\x00\x02S\x05\x00\x03',
              b'S\x05\x00\x03S\x05\x00\x00']
    # lcd control codes
    __display_lcd = ['M\f\0\20', 'M\f\1\20']
    __disable_lcd = b'M^\0\n'
    __enable_lcd = b'M^\1\n'
    __prepare_lcd = b'M^\1'
    __init_lcd = b'M\0'
    __serial = None

    def __init__(self, port='/dev/ttyS1'):
        # Qnap connects its lcd to /dev/ttys1 by default
        self.port = port

    def init(self):
        """
        Initialize the LCD controller
        """
        self.__serial = serial.Serial(self.port, 1200)
        self.__serial.write(self.__init_lcd)
        initlcd = self.__serial.read(4)

        if initlcd != 'S\x01\x00}':
            return False
        return True

    def write(self, row, text):
        """
        Write text to the LCD
        """
        if row in (0, 1):
            writerow = '%s%s' % (self.__display_lcd[row], text.ljust(16)[:16])
            self.__serial.write(self.__prepare_lcd)
            self.__serial.write(writerow.encode())

    def read(self):
        """
        Read a keypress from the panel
        """
        key = self.__serial.read(8)
        if key in self.__down:
            state = 'Down'
        elif key in self.__up:
            state = 'Up'
        elif key in self.__both:
            state = 'Both'
            # Ignore next event as it is always bogus after both keys are
            # pressed.
            self.__serial.read(8)
        else:
            print("Unknown key: ", key)
            state = 'unknown'
        return state

    def enable(self):
        """
        Enable LCD backlight
        """
        self.__serial.write(self.__enable_lcd)

    def disable(self):
        """
       Disable LCD backlight
        """
        self.__serial.write(self.__disable_lcd)
