#!/usr/bin/env python

from setuptools import setup

setup(
    name='swarms-sdk',
    version='0.13',
    description='The Swarms API SDK',
    url='http://github.com/swarms/python-sdk',
    author='Swarms Technologies',
    license='MIT',
    packages=[
        'swarms',
        'swarms.sdk',
        'swarms.sdk.utils',
    ],
    install_requires=[
        'requests',
        'python-magic',
    ],
)
