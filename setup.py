#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='ragnar',
    version='0.1',
    url='https://github.com/mrsmn/ragnar',
    download_url='https://github.com/mrsmn/ragnar/archive/master.zip',
    author='Martin Simon',
    author_email='me@martinsimon.me',
    license='Apache v2.0 License',
    packages=['ragnar'],
    description='Run a function in a separate thread.',
    long_description=file('README.md','r').read(),
    keywords=['thread', 'threading', 'GIL', 'async', 'sync'],
)
