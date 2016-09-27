#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup, find_packages
setup(
    name='simple_ioc',
    version='0.9.0',
    packages=find_packages(),
    url='',
    license='',
    author='Julian Szulc',
    author_email='simple_ioc@julian.net.pl',
    description='Simple IoC for Python',
    install_requires=['dependency_injector']
)
