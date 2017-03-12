# pyBA63
Handle BA63 USB HID line display with ease.

```python
# How to initialise device
from ba63 import BA63
from ba63.constant import SEQUENCE_CHARSET_FR
from time import sleep

my_device = BA63.get()

if my_device is None:
    print('BA63 USB display was not found.')

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