# -*- coding: utf-8 -*-
"""TODO: doc module"""


import logging
from unittest import TestCase
from unittest import skip
from qatestlink.core.testlink_manager import TestlinkManager
#from xml.etree.ElementTree import Element
#from qatestlink.core.TlConnectionBase import TlConnectionBase
#from qatestlink.core.xmls.XmlParserBase import XmlParserBase
#from qatestlink.core.objects.TlTestProject import TlTestProject
#from tests.config import Config


class TestModule(TestCase):
    """TODO: doc class"""

    @classmethod
    def setUpClass(cls):
        cls.testlink_manager = TestlinkManager()

    def setUp(self):
        self.assertIsInstance(
            self.testlink_manager, TestlinkManager)
        self.assertIsInstance(
            self.testlink_manager.log, logging.Logger)

    def test000_conn_ok_bysettings(self):
        """TODO: doc method"""
        self.testlink_manager.api_login()

    @skip("Testcase not ready to be executed yet")
    def test001_conn_ok_byparam(self):
        """TODO: doc method"""
        self.testlink_manager.api_login(
            dev_key='ae2f4839476bea169f7461d74b0ed0ac')

    @skip("Testcase not ready to be executed yet")
    def test002_conn_ko_byparam(self):
        """TODO: doc method"""
        self.assertRaises(
            Exception,
            self.testlink_manager.api_login,
            dev_key='WILLFAIL')
