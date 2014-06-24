#!/usr/bin/env python2

from distutils.core import setup

setup(name='ssdc',
      version='1.0.0',
      description='Clusters files based on their ssdeep hash',
      author='Brian Wallace',
      author_email='bwall@ballastsecurity.net',
      url='https://github.com/bwall/ssdc',
      requires=['pydeep'],
      scripts=['ssdc'],
     )