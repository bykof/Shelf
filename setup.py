#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import Shelf
version = Shelf.__version__

setup(
    name='Shelf',
    version=version,
    author='',
    author_email='mbykovski@seibert-media.net',
    packages=[
        'Shelf',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['Shelf/manage.py'],
)
