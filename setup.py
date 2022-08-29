#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='time_derivative',
    version='1.0.0',
    description='Display the changes that happened in a directory over the course of time.',
    long_description=open('README.md').read(),
    author='Pritom Sarker',
    author_email='pritoms@gmail.com',
    url='https://github.com/pritoms/Time-Derivative',
    license=open('LICENSE').read(),
    packages=find_packages(),
    install_requires=['termcolor'],
    entry_points={
        'console_scripts': [
            'time_derivative = time_derivative:main',
            'time_derivatives = time_derivatives:main',
        ]
    },
)
