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
    down = [b'S\x05\x00\x02S\x05\x00\x00', b'S\x05\x00\x00S\x05\x00\x02', b'S\x05\x00\x02S\x05\x00\x00']
    up   = [b'S\x05\x00\x01S\x05\x00\x00', b'S\x05\x00\x00S\x05\x00\x01', b'S\x05\x00\x01S\x05\x00\x00']
    both = [b'S\x05\x00\x01S\x05\x00\x03', b'S\x05\x00\x02S\x05\x00\x03', b'S\x05\x00\x03S\x05\x00\x00']

    def Init(self):
        self.ser.write('M\0'.encode())
        initlcd = self.ser.read(4)
        if initlcd == 'S\x01\x00}':
            return True

    def Write(self, row, text):
        if row == 0:
            initrow = 'M\f\0\20'
        elif row == 1:
            initrow = 'M\f\1\20'
        writerow = '%s%s' % (initrow, text.ljust(16)[:16])
        self.ser.write('M^\1'.encode())
        self.ser.write(writerow.encode())

    def Read(self):
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
            print("Unknown key: ", read)
            state = 'unknown'
        return state

    def Enable(self):
        self.ser.write('M^\1\n'.encode())

    def Disable(self):
        self.ser.write('M^\0\n'.encode())
