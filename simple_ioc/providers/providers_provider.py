# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from dependency_injector.providers import Provider


class ProvidersProvider(Provider):
    __slots__ = ['providers']

    def _provide(self, *args, **kwargs):
        return map(lambda p: p(), self.providers)

    def __init__(self, providers):
        self.providers = providers
        super(ProvidersProvider, self).__init__()
