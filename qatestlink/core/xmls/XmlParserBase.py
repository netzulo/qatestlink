"""TODO: doc module"""


from xml.etree.ElementTree import ElementTree


class XmlParserBase(object):
    """TODO: doc class"""

    xml = None


    def __init__(self, xml=None):
        """TODO: doc method"""
        if xml is None:
            raise Exception('can\'t parse None XML text')
        self.xml = ElementTree(element=xml)
    
