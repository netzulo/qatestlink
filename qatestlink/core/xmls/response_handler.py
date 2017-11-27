# -*- coding: utf-8 -*-
"""TODO: doc module"""


from xml.etree.ElementTree import tostring as xml_to_str
from qatestlink.core.xmls.base_handler import BaseHandler


class ResponseHandler(BaseHandler):
    """TODO: doc class"""

    def __init__(self, log):
        """Instance handler"""
        super(ResponseHandler, self).__init__(log)

    def create(self, route_type, xml_str):
        """Create response by router_type"""
        super(ResponseHandler, self).is_route_type(route_type)
        root = self.xml_parse(xml_str)
        return xml_to_str(root)
