#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='pearl',
      version='0.1.0',
      packages=find_packages(),
      description='to research the best algorithm and parameters implementing AI algorithms & pipelines',
      author='Bertan Ulusoy',
      author_email='bertan_ulusoy@yahoo.com',
      url='https://github.com/egeai/pearl',
      # packages=['pearl', 'pearl.algorithms'],
      install_requires=['requests=2.27.1', 'pandas==1.4.0', 'numpy==1.22.1', 'scikit-learn==1.0.2'],
      license='MIT',
     )