#!/usr/bin/env python
import serial


class QnapDisplay:
    """
    A simple class to write/read from the LCD Display on a Qnap TS-459 and other Qnaps
    2014 Bkram
    """

    # Qnap connects its serial to ttys1
    ser = serial.Serial('/dev/ttyS1', 1200)

    # 8 bit keycodes from serial controller
    down = ['5305000253050000', '5305000053050002']
    up = ['5305000153050000', '5305000053050001']
    both = ['5305000153050003', '5305000253050003', '5305000353050000']

    def Init(self):
        self.ser.write('M\0')
        initlcd = self.ser.read(4).encode('hex')
        if initlcd == '5301007d':
            return True

    def Write(self, row, text):
        if row == 0:
            initrow = 'M\f\0\20'
        elif row == 1:
            initrow = 'M\f\1\20'
        writerow = '%s%s' % (initrow, text.ljust(16)[:16])
        self.ser.write('M^\1')
        self.ser.write(writerow)

    def Read(self):
        read = self.ser.read(8)
        key = read.encode('hex')
        if key in self.down:
            state = 'Down'
        elif key in self.up:
            state = 'Up'
        elif key in self.both:
            state = 'Both'
            # Ignore next event as it is always bogus after both keys are
            # pressed.
            self.ser.read(8)
        return state

    def Enable(self):
        self.ser.write('M^\1\n')

    def Disable(self):
        self.ser.write('M^\0\n')
