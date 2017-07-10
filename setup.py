from setuptools import setup
import distutils.command.sdist

from pkg_resources import Distribution
from distutils.dist import DistributionMetadata
import setuptools.command.sdist

# Patch setuptools' sdist behaviour with distutils' sdist behaviour
setuptools.command.sdist.sdist.run = distutils.command.sdist.sdist.run

setup(name='opendxl-joesandbox',
      version='0.9.1',
      description='Joe Sandbox Integration with McAfee TIE over DXL',
      # Application author details:
      author="Scott Brumley",
      # License
      license="Apache License 2.0",
      keywords=['opendxl', 'dxl', 'mcafee', 'client', 'tie','joesandbox'],
      url='https://github.com/scottbrumley/opendxl-joesandbox',
      install_requires=['requests'],
      long_description=open('Readme.md').read(),

      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      )

