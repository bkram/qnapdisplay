from setuptools import setup

setup(name='qnapdisplay',
      version='0.1',
      description='Library for interacting with front-panel displays on Qnap products',
      url='http://github.com/bkram/qnapdisplay',
      author='Mark de Bruijn',
      license='GPL2',
      packages=['qnapdisplay'],
      install_requires=['pyserial'])
