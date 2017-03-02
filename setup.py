"""Setup for the lazyimport package."""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import versioneer

with open('README.rst') as f:
    README = f.read()

setup(
    author="Shay Palachy",
    author_email="shaypal5@gmail.com",
    name='lazyimport',
    description="lazyimport lets you import python modules lazily.",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    long_description=README,
    url='https://github.com/shaypal5/lazyimport',
    packages=find_packages(),
    install_requires=[],
    test_suite='nose.collector',
    tests_require=['nose'],
)
