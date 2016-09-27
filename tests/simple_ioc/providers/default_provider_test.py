# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from simple_ioc.providers.default_provider import DefaultProvider
from dependency_injector.errors import Error


class DefaultProviderTest(unittest.TestCase):
    def test_if_default_provider_can_be_initialised(self):
        provider = DefaultProvider()
        self.assertIsInstance(provider, DefaultProvider)

    def test_if_throws_exception_when_called(self):
        provider = DefaultProvider('foo_bar')
        with self.assertRaises(Error) as context:
            provider()
        self.assertEqual('Service foo_bar is not defined.', context.exception.message)
