#!/usr/bin/env python

from setuptools import setup

setup(
    name='swarms_sdk',
    version='0.1',
    description='The Swarms API SDK',
    url='http://github.com/swarms/python-sdk',
    author='Swarms Technologies',
    license='MIT',
    packages=[
        'swarms',
    ],
    install_requires=[
        'requests',
    ],
)
