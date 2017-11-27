# -*- coding: utf-8 -*-
"""TODO: doc module"""

from qatestlink.core.xmls.route_type import RouteType
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import fromstring as xml_from_str
from xml.etree.ElementTree import tostring as xml_to_str


MSG_CREATED_ELEMENT = "Created element named: '{}'"
MSG_CREATED_SUBELEMENT = "Created subelement named: '{}'"
MSG_ADDED_TEXT = "Added text to element: tag={}, text={}"
MSG_CREATED_XMLREQUEST = "Created XML request: \n {}"
MSG_FOUND_NODE = "Found node: tag={}, text={}"
MSG_CREATED_XMLPARAM = "Created XML param: \n {}"


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
        root = self.create_node('methodCall')
        self.create_node(
            'methodName', parent=root, text=route_type.value)
        self.create_node('params', parent=root)
        self.log.info(MSG_CREATED_XMLREQUEST.format(xml_to_str(root)))
        return xml_to_str(root)

    def add_param(self, req_str, param_type, param_name, param_value):
        """
        Add param to created xml request
         obtained as string
        """
        root = self.request_parse(req_str).getroot()
        self.log.debug("Adding param:")
        self.log.debug("    type={}".format(param_type))
        self.log.debug("    name={}".format(param_name))
        self.log.debug("    value={}".format(param_value))
        n_params = self.find_node('params', parent=root)
        n_param = self.create_node('param', parent=n_params)
        n_value = self.create_node('value', parent=n_param)
        # TODO: type XML validation for params
        # just struct handleded
        if param_type == 'struct':
            n_struct = self.create_node('struct', parent=n_value)
            n_member = self.create_node('member', parent=n_struct)
            n_name = self.create_node(
                'name', parent=n_member, text=param_name)
            n_value = self.create_node('value', parent=n_member)
            n_value_string = self.create_node(
                'string', parent=n_value, text=param_value)
        else:
            raise Exception('param_type not supported, can\'t add_param')
        self.log.info(MSG_CREATED_XMLPARAM.format(xml_to_str(root)))
        return xml_to_str(root)

    def create_node(self, tag, parent=None, text=None):
        """
        Create XML node element
         and subelement if parent is obtained
        """
        node = None
        if parent is None:
            node = Element(tag)
            self.log.debug(
                MSG_CREATED_ELEMENT.format(tag))
        else:
            node = SubElement(parent, tag)
            self.log.debug(
                MSG_CREATED_SUBELEMENT.format(tag))
        if text is not None:
            node.text = text
            self.log.debug(
                MSG_ADDED_TEXT.format(tag, text))
        return node

    def find_node(self, tag, request=None, parent=None):
        """
        Returns firt node obtained iter
         by tag name on string 'request'
        """
        err_msg = 'Can\'t use this function like this, read documentation'
        if request is None and parent is None:
            raise Exception(err_msg)
        if request is not None and parent is not None:
            raise Exception(err_msg)
        if parent is not None:
            root = parent
        if request is not None:
            root = self.request_parse(request)
        # Search element
        for node in ElementTree(element=root).iter(tag=tag):
            if node.tag == tag:
                self.log.debug(MSG_FOUND_NODE.format(node.tag, node.text))
                return node

    def request_parse(self, request):
        """
        Parse request string and return it
        """
        self.log.debug("Parsing xml:")
        self.log.debug("    from={}".format(request))
        root = ElementTree(xml_from_str(request))
        self.log.debug("    to={}".format(root))
        return root
