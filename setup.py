#!/usr/bin/env python

from distutils.core import setup

setup(name='PlayNinjaLegends',
      version='0.0.2',
      description='Ninja Legends',
      author='wobm',
      author_email='wobm@teknik.io',
      packages=['playninjalegends'],
      install_requires=['Py3AMF', 'licensing', 'requests', 'pyarmor']
      )
