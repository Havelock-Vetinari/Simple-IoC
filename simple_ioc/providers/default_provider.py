#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from dependency_injector.errors import Error
from dependency_injector.providers import Provider


class DefaultProvider(Provider):
    def __init__(self, service_name='Unknown'):
        self.service_name = service_name
        super(DefaultProvider, self).__init__()

    def _provide(self, *args, **kwargs):
        raise Error('Service %s is not defined.' % self.service_name)
