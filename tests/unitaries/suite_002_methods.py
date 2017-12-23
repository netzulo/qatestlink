# -*- coding: utf-8 -*-
"""TODO: doc module"""


import logging
from unittest import TestCase
from unittest import skip
from qatestlink.core.testlink_manager import TLManager
from qatestlink.core.models.tl_models import TProject
API_DEV_KEY = 'ae2f4839476bea169f7461d74b0ed0ac'


class TestMethods(TestCase):
    """TODO: doc class"""

    @classmethod
    def setUpClass(cls):
        """TODO: doc method"""
        cls.testlink_manager = TLManager()

    def setUp(self):
        """TODO: doc method"""
        self.assertIsInstance(
            self.testlink_manager, TLManager)
        self.assertIsInstance(
            self.testlink_manager.log, logging.Logger)
    
    def test_001_method_gettprojects(self):
        """TODO: doc method"""
        tprojects = self.testlink_manager.api_get_tprojects(
            dev_key=API_DEV_KEY)
        self.assertIsInstance(tprojects, list)
        self.assertGreater(len(tprojects), 0)
        self.assertIsInstance(tprojects[0], TProject)
        for tproject in tprojects:
            self.testlink_manager.log.debug(repr(tproject))


class TestMethodsRaises(TestCase):
    """TODO: doc class"""

    @classmethod
    def setUpClass(cls):
        """TODO: doc method"""
        cls.testlink_manager = TLManager()

    def setUp(self):
        """TODO: doc method"""
        self.assertIsInstance(
            self.testlink_manager, TLManager)
        self.assertIsInstance(
            self.testlink_manager.log, logging.Logger)