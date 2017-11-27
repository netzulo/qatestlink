# -*- coding: utf-8 -*-
"""TODO: doc module"""


from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import fromstring as xml_from_str
from qatestlink.core.xmls.route_type import RouteType


MSG_CREATED_ELEMENT = "Created element named: '{}'"
MSG_CREATED_SUBELEMENT = "Created subelement named: parent='{}',  tag='{}'"
MSG_ADDED_TEXT = "Added text to element: tag='{}', text='{}'"
MSG_FOUND_NODE = "Found node: tag='{}', text='{}'"
MSG_ROUTE_TYPE_OK = "Valid route_type: '{}'"


class BaseHandler(object):
    """TODO: doc class"""
    log = None

    def __init__(self, log):
        """Instance handler"""
        self.log = log

    def is_route_type(self, route_type):
        """
        This method functionality must be
         complete at inherit classes
        """
        if not isinstance(route_type, RouteType):
            raise Exception('Bad RouteType : {}'.format(route_type))
        self.log.info(MSG_ROUTE_TYPE_OK.format(route_type))
        return True

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
                MSG_CREATED_SUBELEMENT.format(parent.tag, tag))
        if text is not None:
            node.text = text
            self.log.debug(
                MSG_ADDED_TEXT.format(tag, text))
        return node

    def find_node(self, tag, req_str=None, parent=None):
        """
        Returns firt node obtained iter
         by tag name on string 'request'
        """
        err_msg = 'Can\'t use this function like this, read documentation'
        if req_str is None and parent is None:
            raise Exception(err_msg)
        if req_str is not None and parent is not None:
            raise Exception(err_msg)
        if parent is not None:
            root = parent
        if req_str is not None:
            root = self.xml_parse(req_str)
        # Search element
        for node in ElementTree(element=root).iter(tag=tag):
            if node.tag == tag:
                self.log.debug(MSG_FOUND_NODE.format(node.tag, node.text))
                return node

    def xml_parse(self, xml_str):
        """
        Parse request string and return it
        """
        self.log.debug("Parsing xml:")
        self.log.debug("    from={}".format(xml_str))
        root = ElementTree(xml_from_str(xml_str)).getroot()
        self.log.debug("    to={}".format(root))
        return root
