#!/usr/bin/env python
from qnapdisplay import QnapDisplay
import time

Lcd = QnapDisplay()

if Lcd.Init:

    Lcd.Enable()
    Lcd.Write(1, '')

    for x in range(1, 10):

        Lcd.Write(0, 'Enter key %d' % x)

        read = Lcd.Read()
        print('%s pressed' % (read))
        Lcd.Write(1, '%s pressed' % (read))

    Lcd.Write(0, '')
    Lcd.Write(1, '')
    Lcd.Disable()

else:
    print('Oops something went wrong here')
