#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from dependency_injector.containers import DynamicContainer

from simple_ioc.providers.default_provider import DefaultProvider


class DefaultContainer(DynamicContainer):
    def __init__(self):
        self._services = dict()
        super(DefaultContainer, self).__init__()

    def __getattr__(self, item):
        if item not in self._services:
            self._services[item] = DefaultProvider(item)
        return self._services[item]
