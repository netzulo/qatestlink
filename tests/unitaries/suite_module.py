# -*- coding: utf-8 -*-
"""TODO: doc module"""


import logging
from unittest import TestCase
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

    def test000_connection_ok(self):
        """TODO: doc method"""
        self.testlink_manager.api_login()

"""
    def test_001_xmlbase_instance(self):
        ""TODO: doc method""
        xml_parser = XmlParserBase()
        self.assertIsInstance(xml_parser, XmlParserBase)
        self.assertIsInstance(xml_parser.xml, Element)

    def test_002_xmlbase_prettify(self):
        ""TODO: doc method""
        xml_parser = XmlParserBase()
        xml_print = xml_parser.prettify()
        self.assertIsNotNone(xml_print)

    def test_003_connection_with_devkey(self):
        ""TODO: doc method""
        testlink = TlConnectionBase(
            url=self.config.url,
            dev_key=self.config.dev_key
        )
        self.assertIsInstance(testlink, TlConnectionBase)
        res = testlink.check_dev_key()
        self.assertIsNotNone(res)
        self.assertTrue(res.logged)

    def test_004_connection_failed(self):
        ""TODO: doc method""
        testlink = TlConnectionBase(
            url=self.config.url,
            dev_key='failed'
        )
        self.assertIsInstance(testlink, TlConnectionBase)
        self.assertRaises(Exception, testlink.check_dev_key)

    def test_005_tprojects(self):
        ""TODO: doc method""
        testlink = TlConnectionBase(
            url=self.config.url,
            dev_key=self.config.dev_key
        )
        res = testlink.test_projects()
        self.assertIsNotNone(res)
        self.assertIsInstance(res.test_projects[0], TlTestProject)
        self.assertIsInstance(res.test_projects[1], TlTestProject)
"""