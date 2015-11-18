#!/usr/bin/env python
from qnapdisplay import QnapDisplay
import time

Lcd = QnapDisplay()

if Lcd.Init:
    Lcd.Write(0, 'Qnap Display')
    Lcd.Write(1, 'Press a key')

    read = Lcd.Read()
    Lcd.Write(1, '%s pressed' % (read))
    time.sleep(2)

    Lcd.Write(0, 'On and Off')
    Lcd.Write(1, '10 times')

    for x in range(0, 10):

        Lcd.Disable()
        time.sleep(4)
        Lcd.Enable()
        time.sleep(4)

    Lcd.Enable()
    Lcd.Write(0, 'Stay a while')
    Lcd.Write(1, 'Stay forever')

else:
    print 'Oops something went wrong here'
