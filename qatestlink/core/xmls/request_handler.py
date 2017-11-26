# -*- coding: utf-8 -*-
"""TODO: doc module"""

from qatestlink.core.xmls.route_type import RouteType
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import fromstring as xml_from_str
from xml.etree.ElementTree import tostring as xml_to_str

class RequestHandler(object):
    """TODO: doc class"""
    log = None


    def __init__(self, log):
        """Instance handler"""
        self.log = log

    def create(self, route_type):
        """
        Create XML string ready to use
         on requests
        """
        if not isinstance(route_type, RouteType):
            raise Exception('Bad RouteType : {}'.format(route_type))
        root = Element('methodCall')
        self.log.debug(
            "Created element named: 'methodCall'")
        method_name = SubElement(root, 'methodName')
        self.log.debug(
            "Created subelement named: 'methodName'")
        method_name.text = route_type.value
        SubElement(root, 'params')
        self.log.debug(
            "Created subelement named: 'params'")
        xml_str = xml_to_str(root)
        self.log.debug(
            "Create XML request: \n {}".format(xml_str))
        return xml_str

    def add_param(self, request, param_type, param_name, param_value):
        """
        Add param to created xml request
         obtained as string
        """
        root = self.request_parse(request)
        n_params = self.find_node('params', parent=root)
        n_param = self.create_node('param', parent=n_params)
        n_value = self.create_node('value', n_param)
        # TODO: type XML validation for params
        # just struct handleded
        if param_type == 'struct':
            n_struct = self.create_node('struct', n_value)
            n_member = self.create_node('member', n_struct)
            n_name = self.create_node('name', n_member)
            n_name.text = param_name
            n_value = self.create_node('value', n_member)
            n_value_string = self.create_node('string', n_value)
            n_value_string.text = param_value

        else:
            raise Exception('param_type not supported, can\'t add_param')
        return root

    def create_node(self, tag, parent=None):
        """
        Create XML node element
         and subelement if parent is obtained
        """
        if parent is None:
            return Element(tag)
        else:
            return SubElement(parent, tag)


    def find_node(self, tag, request=None, parent=None):
        """
        Returns firt node obtained iter
         by tag name on string 'request'
        """
        if request is not None and parent is not None:
            raise Exception(
                'Can\'t use this function like this, read documentation')
        root = self.request_parse(request)
        for node in root.iter(tag=tag):
            return node
        

    def request_parse(self, request):
        """
        Parse request string and return it
        """
        return ElementTree(xml_from_str(request))
