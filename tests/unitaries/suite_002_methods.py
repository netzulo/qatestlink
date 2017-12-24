# -*- coding: utf-8 -*-
"""TODO: doc module"""


import logging
from unittest import TestCase
from unittest import skipIf
from qatestlink.core.xmls.error_handler import ResponseException
from qatestlink.core.testlink_manager import TLManager
from qatestlink.core.models.tl_models import TProject

API_DEV_KEY = 'ae2f4839476bea169f7461d74b0ed0ac'
SKIP = False

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

    @skipIf(SKIP, 'Test SKIPPED')
    def test_001_method_gettprojects(self):
        """TODO: doc method"""
        tprojects = self.testlink_manager.api_tprojects(
            dev_key=API_DEV_KEY)
        self.assertIsInstance(tprojects, list)
        self.assertGreater(len(tprojects), 0)
        for tproject in tprojects:
            self.testlink_manager.log.debug(repr(tproject))
            self.assertIsInstance(tprojects[0], TProject)

    @skipIf(SKIP, 'Test SKIPPED')
    def test_002_method_gettprojectbyname(self):
        """TODO: doc method"""
        tproject_name = 'qacode'
        tproject = self.testlink_manager.api_tproject(tproject_name)
        self.assertIsInstance(tproject, TProject)
        self.assertEquals(tproject.name, tproject_name)

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

    @skipIf(SKIP, 'Test SKIPPED')
    def test_002_raises_gettprojectbyname_notname(self):
        """TODO: doc method"""
        self.assertRaises(Exception, self.testlink_manager.api_tproject)
    
    @skipIf(SKIP, 'Test SKIPPED')
    def test_003_raises_gettprojectbyname_emptyname(self):
        """TODO: doc method"""
        self.assertRaises(ResponseException, self.testlink_manager.api_tproject, '')