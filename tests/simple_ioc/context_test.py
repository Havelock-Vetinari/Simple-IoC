# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from dependency_injector.providers import Object

from simple_ioc.containers.default_container import DefaultContainer
from simple_ioc.context import Context


class ContextTest(unittest.TestCase):
    def test_if_get_container_returns_same_container(self):
        container = Context.get_container()
        self.assertIsInstance(container, DefaultContainer)
        self.assertEqual(container, Context.get_container())

    def test_overriding_services_with_context(self):
        with Context.provide_services() as container:
            container.sample_service = Object('Hello, World!')
        self.assertEqual('Hello, World!', Context.get_container().sample_service())
