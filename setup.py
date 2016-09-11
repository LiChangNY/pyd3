#! /usr/bin/env python
# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='jarvis',
      version='0.1',
      description="Python - Just another visualization library built on top of d3.js",
      py_modules=['jarvis'],
      author='Lily Chang',
      author_email='changliemail@gmail.com',
      url='https://github.com/LiChangNY/jarvis',
      )