# -*- coding: utf-8 -*-
# pylint: disable=no-self-use
# pylint: disable=useless-super-delegation
"""TODO: doc module"""


from unittest import TestCase
from xml.etree.ElementTree import Element
from qatestlink.core.TlConnectionBase import TlConnectionBase
from qatestlink.core.xmls.XmlParserBase import XmlParserBase


class TestModule(TestCase):
    """TODO: doc class"""

    def __init__(self, method_name='TestModule'):
        """TODO: doc method"""
        super(TestModule, self).__init__(method_name)


    def test_000_dummytest(self):
        """TODO: doc method"""
        print("Library must can be installed, but not really tested")


    def test_001_xmlbase_instance(self):
        """TODO: doc method"""
        xml_parser = XmlParserBase()
        self.assertIsInstance(xml_parser, XmlParserBase)
        self.assertIsInstance(xml_parser.xml, Element)


    def test_001_connection_with_devkey(self):
        """"TODO: doc method"""
        testlink = TlConnectionBase(
            url='http://qalab.tk:86/lib/api/xmlrpc/v1/xmlrpc.php',
            dev_key='ae2f4839476bea169f7461d74b0ed0ac'
        )
        print(testlink.check_dev_key())
