#!/usr/bin/env python
import os
from setuptools import setup

from electron import __version__

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="python-electron",
    version=__version__,
    description="A python interface for Apache Electron CLI",
    long_description=README,
    author="Oshane Bailey",
    author_email="b4.oshany@gmail.com",
    url="http://github.com/talpor/python-cordova",
    packages=['electron'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
        'Topic :: Utilities',
    ],
    keywords=['python', 'electron'  , 'electron-packager', 'electron-app']
)
