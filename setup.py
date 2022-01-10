"""
Qnapdisplay, an lcd python module for Qnap.
Features both writing to the display as wel as reading key presses from the front panel.
It was developed on a Qnap TS-459, but it will work on some other models as well.
"""
from setuptools import setup

setup(name='qnapdisplay',
      version='0.2',
      description='Library for interacting with front-panel displays on Qnap products',
      url='http://github.com/bkram/qnapdisplay',
      author='Mark de Bruijn',
      license='GPL2',
      packages=['qnapdisplay'],
      install_requires=['pyserial'])
