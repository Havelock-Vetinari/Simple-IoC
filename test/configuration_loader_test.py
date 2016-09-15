# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from simple_py_ioc.configuration_loader import ConfigurationLoader
from dependency_injector.containers import DynamicContainer


class ConfigurationLoaderTestCase(unittest.TestCase):
    def test_getting_container(self):
        configuration_loader = ConfigurationLoader()
        self.assertIsInstance(configuration_loader.get_container(), DynamicContainer)

    def test_configure_hello_string(self):
        configuration = {
            'simple_service': {
                'factory_class': 'dependency_injector.providers.base.Object',
                'factory_arguments': 'Hello, World!'
            }
        }

        configuration_loader = ConfigurationLoader()
        configuration_loader.load_services_configuration(configuration)
        container = configuration_loader.get_container()

        self.assertEqual(container.simple_service(), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
