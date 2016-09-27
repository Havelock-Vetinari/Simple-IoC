# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from dependency_injector.providers import Object

from simple_ioc.providers.providers_provider import ProvidersProvider
from simple_ioc.containers.default_container import DefaultContainer
from dependency_injector.containers import DynamicContainer



class DefaultProviderTest(unittest.TestCase):
    def test_if_provider_resolves_provided_providers(self):
        provider = ProvidersProvider([Object('Hello, World!'), Object(42)])
        self.assertListEqual(['Hello, World!', 42], provider())

    def test_if_provided_providers_are_overriden_by_other_providers(self):
        container = DefaultContainer()

        container.services_service = ProvidersProvider([
            container.sub_service_1,
            container.sub_service_2
        ])

        overriding_container = DynamicContainer()
        overriding_container.sub_service_1 = Object('Hello')
        overriding_container.sub_service_2 = Object('World')
        container.override(overriding_container)

        self.assertListEqual(['Hello', 'World'], container.services_service())
