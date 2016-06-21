#!/usr/bin/env python

from setuptools import setup

setup(name='recipes',
      version='0.1',
      description='Recipes Utilities',
      author='Brandon Davis',
      author_email='admin@redspin.net',
      packages=['recipes'],
      install_requires=[
      ],
      entry_points = {
          'console_scripts': ['recipes=recipes.cli:main']
      })