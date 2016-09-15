# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from dependency_injector.containers import DynamicContainer
from dependency_injector.providers import Object


class ConfigurationLoader:
    def __init__(self):
        self.container = DynamicContainer()

    def load_services_configuration(self, configuration):
        for service_name, service_info in configuration.items():
            provider_arguments = service_info['factory_arguments']
            setattr(self.container, service_name, Object(provider_arguments))

    def get_container(self):
        return self.container
