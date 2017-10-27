# -*- coding: utf-8 -*-
"""TODO: doc module"""

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring as xml_to_string
from qatestlink.core.xmls.XmlParserBase import XmlParserBase


class XmlParserRequest(XmlParserBase):
    """TODO: doc class"""

    dev_key = None
    method_name = None
    root = None
    params = None

    def __init__(self, xml_path=None, xml_str=None, dev_key=None, method_name=None):
        """TODO: doc method"""
        super(XmlParserRequest, self).__init__(xml_path=None, xml_str=None)

        if dev_key is None:
            raise Exception(
                'Can\'t parse XmlRequest if dev_key it\'s None')
        self.dev_key = dev_key
        if method_name is None:
            raise Exception(
                'Can\'t parse XmlRequest if method_name it\'s None')
        self.method_name = method_name
        self.root = self.xml.getroot()
        #####
        method_call = self.find_node('methodCall')
        node_method_name = self.create_node('methodName', parent=method_call)
        node_method_name.text = self.method_name
        self.params = self.create_node('params', parent=method_call)
        self.create_param(
            method_name='devKey',
            method_type='string',
            method_value=self.dev_key)

    def create_node(self, tag, parent=None, add_root=False, text=None):
        """TODO: doc method"""
        msg_tmpl = "Added element='{}' to parent='{}'"
        node = Element(tag)
        if text is not None:
            node.text = text
        if add_root:
            self.root.append(node)
            print(msg_tmpl.format(tag, self.root.tag))
        if parent is not None:
            parent.append(node)
            print(msg_tmpl.format(tag, parent.tag))
        return node

    def find_node(self, tag):
        """TODO: doc method"""
        for node in self.root.iter(tag=tag):
            print("Found element tag='{}'".format(tag))
            return node


    def create_param(self, method_name=None, method_type=None, method_value=None):
        """TODO: doc method"""
        if method_name is None:
            method_name = self.method_name
        if method_type not in ['string']:
            raise Exception("Method type value not selected at create_param")
        param = self.create_node('param', parent=self.params)
        value = self.create_node('value', parent=param)
        struct = self.create_node('struct', parent=value)
        member = self.create_node('member', parent=struct)
        self.create_node('name', parent=member, text=method_name)
        value_type = self.create_node('value', parent=member)
        self.create_node(method_type, parent=value_type, text=method_value)

    def to_string(self):
        """TODO: doc method"""
        return xml_to_string(self.root)
