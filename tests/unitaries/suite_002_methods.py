# -*- coding: utf-8 -*-
"""TODO: doc module"""


import logging
from unittest import TestCase
from unittest import skipIf
from qatestlink.core.xmls.error_handler import ResponseException
from qatestlink.core.testlink_manager import TLManager
from qatestlink.core.models.tl_models import TProject
from qatestlink.core.models.tl_models import TPlan


API_DEV_KEY = 'ae2f4839476bea169f7461d74b0ed0ac'
SKIP = False
CONFIG = {
    "tproject_name": "qacode",
    "tproject_id" : 11
}


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
    def test_001_method_tprojects(self):
        """TODO: doc method"""
        tprojects = self.testlink_manager.api_tprojects(
            dev_key=API_DEV_KEY)
        self.assertIsInstance(tprojects, list)
        self.assertGreater(len(tprojects), 0)
        for tproject in tprojects:
            self.testlink_manager.log.debug(repr(tproject))
            self.assertIsInstance(tproject, TProject)

    @skipIf(SKIP, 'Test SKIPPED')
    def test_002_method_tproject(self):
        """TODO: doc method"""
        tproject = self.testlink_manager.api_tproject(CONFIG['tproject_name'])
        self.assertIsInstance(tproject, TProject)
        self.assertEquals(tproject.name, CONFIG['tproject_name'])

    @skipIf(SKIP, 'Test SKIPPED')
    def test_003_method_tproject_tplans(self):
        """TODO: doc method"""
        tplans = self.testlink_manager.api_tproject_tplans(CONFIG['tproject_id'])
        self.assertIsInstance(tplans, list)
        self.assertGreater(len(tplans), 0)
        for tplan in tplans:
            self.testlink_manager.log.debug(repr(tplan))
            self.assertIsInstance(tplan, TPlan)

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
    def test_001_raises_tproject_notname(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tproject)
    
    @skipIf(SKIP, 'Test SKIPPED')
    def test_002_raises_tproject_emptyname(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tproject,
            '')
    
    @skipIf(SKIP, 'Test SKIPPED')
    def test_003_raises_tproject_tplans_notid(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception, self.testlink_manager.api_tproject_tplans)

    @skipIf(SKIP, 'Test SKIPPED')
    def test_004_raises_tproject_tplans_notfoundid(self):
        """TODO: doc method"""
        self.assertRaises(
            ResponseException,
            self.testlink_manager.api_tproject_tplans,
            -1)