# Qnapdisplay

Qnap lcd python module, features both writing to the display as wel as reading key presses from the front panel. It was
developed on a Qnap TS-459, but it will work on some other models as well.

## Supported Systems

Qnap systems that are known to work:

- TS-453A
- TS-459
- TVS-872X

## Module install

```bash
sudo pip install git+https://github.com/bkram/qnapdisplay.git
```

## Acknowledgements

Thanks to the following persons:

- daald for sending a PR and letting know it works with the TS-453A
- sigio for letting know it works with the TVS-872X

## Future

As my own lcd has died, I can no longer maintain it myself, contributions are of course welcomed.

## Breaking changes in 0.2

In version 0.2 the classes have been renamed to conform the python standards.

This means the functions in the QnapDisplay class have been refactored to the following:

- init
- write
- read
- enable
- disable

In your old code you will need to make the function calls lower case.

## New feature

It is now possible specify a serial port, of your lcd is not connected to /dev/ttyS1, or if you are running Windows

## Example using serial port /dev/ttyS2

```python
from qnapdisplay import QnapDisplay

lcd = QnapDisplay(port='/dev/ttyS2')
```