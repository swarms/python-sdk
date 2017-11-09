#!/usr/bin/env python

from setuptools import setup

setup(
    name='swarms_sdk',
    version='0.2',
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
    ],
)
