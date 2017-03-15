from distutils.core import setup

setup(
    name='pyBA63',
    packages=['ba63'],
    version='0.1.6',
    license='MIT',
    description='Manage BA63 USB HID line display easily',
    author='Ahmed TAHRI',
    author_email='ahmed@tahri.space',
    url='https://github.com/Ousret/pyBA63',
    download_url='https://github.com/Ousret/pyBA63/tarball/0.1.6',
    keywords=['wincor nixdorf', 'line display', 'ba63', 'hid'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    requires=['unidecode', 'cython', 'hidapi']
)
