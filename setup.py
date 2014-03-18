#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
atosl: atos for Linux
"""

from setuptools import setup
from distutils.core import setup, Extension

atosl_module = Extension('atosl', ["converter.c", "macho.c", "atosl.c", "python_wrapper.c"])

# atosl.symbolicate('armv7s', 'test/res/CrashTest3Dwarf.fat', ("0x00006ed7", ))
setup(name='atosl',
    # version=__version__,
    version='0.0.1',
    description='atosl: atos for linux',
    long_description=open("README.md").read(),
    author='Reno Qiu',
    author_email='dechao.qiu@gmail.com',
    keywords='atos for linux, binary addresses to symbols',
    license="MIT",
    platforms=["Linux, Mac OS X"],
    url='https://github.com/renoqiu/atosl_python',
    download_url='https://github.com/renoqiu/atosl_python',
    ext_modules = [atosl_module],
)

