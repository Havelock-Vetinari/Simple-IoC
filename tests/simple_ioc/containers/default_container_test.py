# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from dependency_injector.containers import DynamicContainer
from dependency_injector.errors import Error
from dependency_injector.injections import inject
from dependency_injector.providers import Object

from simple_ioc.containers.default_container import DefaultContainer
from simple_ioc.providers.default_provider import DefaultProvider


class DefaultContainerTest(unittest.TestCase):
    def test_if_can_create_instance(self):
        self.assertIsInstance(DefaultContainer(), DefaultContainer)

    def test_if_can_use_undefined_yet_services_in_inject_declarations(self):
        container = DefaultContainer()
        self.assertIsInstance(container.foo_service, DefaultProvider)

    def test_if_calling_injection_with_undefined_service_raises_error(self):
        container = DefaultContainer()

        @inject(some_value=container.some_service)
        def sample_injection(some_value):
            return some_value

        with self.assertRaises(Error) as error_context:
            sample_injection()

        self.assertEqual('Service some_service is not defined.',
                         error_context.exception.message)

    def test_if_one_can_define_service(self):
        container = DefaultContainer()

        container.some_service = Object(42)

        @inject(some_value=container.some_service)
        def sample_injection(some_value):
            return some_value

        self.assertEqual(42, sample_injection())

    def test_if_one_can_define_service_after_declaration(self):
        container = DefaultContainer()

        class SomeClass:
            @inject(some_value=container.some_other_service)
            def __init__(self, some_value):
                self.a = some_value

        overriding_container = DynamicContainer()
        overriding_container.some_other_service = Object(42)
        container.override(overriding_container)

        self.assertEqual(42, SomeClass().a)

    def test_if_one_can_define_fresh_service(self):
        container = DefaultContainer()
        overriding_container = DynamicContainer()
        overriding_container.new_service = Object('Hello, World!')
        container.override(overriding_container)
        self.assertEqual('Hello, World!', container.new_service())
