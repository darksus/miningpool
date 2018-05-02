from setuptools import setup, find_packages
__version__ = "1.0.0"
import os

import platform
distro = platform.dist()[0]
distro_major_version = platform.dist()[1].split('.')[0]

data_files = []

with open('requirements.txt') as fd:
    requires = fd.read().splitlines()

setup(name='miningpool',
      author='Spiderman',
      author_email='spiderman@avengers.com',
      url='https://github.com/none/nop',
      version=__version__,
      packages=find_packages(),
      install_requires=requires,
      data_files=data_files,
      entry_points={
          'console_scripts': [
              'miningpool = miningpool.main:main',
          ]})
