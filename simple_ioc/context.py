# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from contextlib import contextmanager

from dependency_injector.containers import DynamicContainer

from simple_ioc.containers.default_container import DefaultContainer


class Context:
    _container = None

    def __init__(self):
        pass

    @classmethod
    def get_container(cls):
        if not cls._container:
            cls._container = cls._build_container()
        return cls._container

    @classmethod
    def _build_container(cls):
        return DefaultContainer()

    @classmethod
    @contextmanager
    def provide_services(cls):
        container = DynamicContainer()
        yield container
        cls.get_container().override(container)
