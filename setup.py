from distutils.core import setup

setup(
    name='pyBA63',
    packages=['ba63'],
    version='0.1.5',
    description='Manage BA63 USB HID line display easily',
    author='Ahmed TAHRI',
    author_email='ahmed@tahri.space',
    url='https://github.com/Ousret/pyBA63',
    download_url='https://github.com/Ousret/pyBA63/tarball/0.1',
    keywords=['wincor nixdorf', 'line display', 'ba63', 'hid'],
    classifiers=[],
    requires=['unidecode', 'cython', 'hidapi']
)
