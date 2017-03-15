# pyBA63 0.1.6
Python based driver for Wincor Nixdorf BA63 USB HID line display.
Most used for point-of-sale.

## Installation

Via PyPi
```sh
pip install pyBA63
```

Via git cloning
```sh
git clone https://github.com/Ousret/pyBA63.git
cd pyBA63/
python setup.py install
```

## Usage
```python
# How to initialise device
from ba63 import BA63
from ba63.constant import SEQUENCE_CHARSET_FR
from time import sleep

my_device = BA63.get()

if my_device is None:
    print('BA63 USB display was not found.')
    exit(1)

# Set charset to FR
my_device.charset(SEQUENCE_CHARSET_FR)

# Write hello world on line 1
my_device.imprimer(1, 'Hello World')

sleep(1)

# Clear display
my_device.nettoyer()

# Write hello world on line 2
my_device.imprimer(2, 'Hello World')

sleep(1)

my_device.nettoyer()

# Close the device
my_device.fermer()
```