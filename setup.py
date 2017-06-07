#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='axpy_selenium',
    version='0.1.0',
    description="Python script that automatically fills in online forms",
    long_description=readme + '\n\n' + history,
    author="Axel Johansson",
    author_email='Axel.Johansson10@gmail.com',
    url='https://github.com/AxxAxx/axpy_selenium',
    packages=[
        'axpy_selenium',
    ],
    package_dir={'axpy_selenium':
                 'axpy_selenium'},
    entry_points={
        'console_scripts': [
            'axpy_selenium=axpy_selenium.mainfile:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='axpy_selenium',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
