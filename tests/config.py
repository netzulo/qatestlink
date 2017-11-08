# -*- coding: utf-8 -*-


from os import environ


ENV_URL = 'TESTLINK_URL'
ENV_DEV_KEY = 'TESTLINK_DEV_KEY'

DEFAULT_ENV_URL = 'http://localhost'

TESTLINK_URL_PATH = 'lib/api/xmlrpc/v1/xmlrpc.php'


class Config(object):
    def __init__(self):
        self._data = {
            'url': '/'.join([
                self._get_var(ENV_URL, DEFAULT_ENV_URL).strip('/'),
                TESTLINK_URL_PATH,
            ]),
            'dev_key': self._get_var(ENV_DEV_KEY),
        }

    def _get_var(self, name, default=None):
        try:
            return environ[name]
        except KeyError:
            if default is not None:
                return default
            raise RuntimeError(
                "You're missing the mandatory environment variable {0!s}, "
                "please see the README.rst file for information about how to "
                "run the tests.".format(name)
            )

    def __getattr__(self, name):
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(name)
