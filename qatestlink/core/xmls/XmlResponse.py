# -*- coding: utf-8 -*-
"""TODO: doc module"""


from qatestlink.core.xmls.XmlParserBase import XmlParserBase
from qatestlink.core.TlRequest import TlRequest as REQUEST
from qatestlink.core.objects.TlTestProject import TlTestProject

class XmlResponse(XmlParserBase):
    """TODO: doc class"""

    logged = None
    test_projects = None

    def __init__(self, xml_path=None, xml_str=None, method_name=None):
        """TODO: doc method"""
        super(XmlResponse, self).__init__(xml_path=xml_path, xml_str=xml_str)
        if method_name is None:
            raise Exception(
                'Can\'t parse XmlRequest if method_name it\'s None')
        self.method_name = method_name
        self.logged = False
        self.test_projects = list()
        self.parse_response()

    def parse_response(self):
        """TODO: doc method"""
        # Check request reponse it's well formed
        if self.find_node('methodResponse') is None:
            raise Exception('Bad Response, not <methodResponse> node')
        # Check request response it's authorized
        self.parse_error()
        if self.method_name == REQUEST.TLINK_CHECK_DEV_KEY.value:
            node = self.find_node('boolean')
            if node is not None:
                self.logged = bool(node.text)
        if self.method_name == REQUEST.TPROJECTS.value:
            node_structs_members = self.find_structs_members()
            for node_struct_members in node_structs_members:
                for node_member in node_struct_members:
                    node_data = self.parse_member(node_member)
                    self.test_projects.append(self.parse_tproject(node_data))

    def parse_tproject(self, node_data):
        """
        Args:
            node_data, must be list of dicts
                {"name": member_name, "value": member_value_parsed}
        """
        test_project = TlTestProject()
        for member in node_data:
            print("parsing testproject, name={}, value={}".format(
                member.get('name'), member.get('value')))
            if member.get('name') == 'id':
                test_project.id = int(member.get('value'))
            if member.get('name') == 'name':
                test_project.name = member.get('value')
            if member.get('name') == 'active':
                test_project.active = member.get('value')
            if member.get('name') == 'is_public':
                test_project.is_public = member.get('value')
            if member.get('name') == 'api_key':
                test_project.api_key = member.get('value')
            if member.get('name') == 'tc_counter':
                test_project.tc_counter = member.get('value')
            if member.get('name') == 'options_reqs':
                test_project.options_reqs = member.get('value')
            if member.get('name') == 'option_priority':
                test_project.option_priority = member.get('value')
            if member.get('name') == 'option_automation':
                test_project.option_automation = member.get('value')
            if member.get('name') == 'issue_tracker_enabled':
                test_project.issue_tracker_enabled = member.get('value')
            if member.get('name') == 'reqmgr_integration_enabled':
                test_project.reqmgr_integration_enabled = member.get('value')
            if member.get('name') == 'options':
                test_project.options = member.get('value')
            if member.get('name') == 'notes':
                test_project.notes = member.get('value')
            if member.get('name') == 'color':
                test_project.color = member.get('value')
            if member.get('name') == 'opt': # struct will do nothing
                test_project.opt = member.get('value')
        return test_project


    def find_structs_members(self):
        """Finds <member> tags on <struct> tag"""
        print('Starting to extract name+value for each member...')
        node_structs_list = list()
        node_data = self.find_node(tag='data')
        nodes_struct = self.find_nodes('struct', parent=node_data)
        for node_struct in nodes_struct:
            node_struct_members = self.find_nodes(tag='member', parent=node_struct)
            node_structs_list.append(node_struct_members)
        return node_structs_list


    def find_member_info(self, node_member):
        """Find <name> and <value> tags on <member> tag"""
        node_name = self.find_node(tag='name', parent=node_member)
        node_value = self.find_node(tag='value', parent=node_member)
        return (node_name, node_value)

    def parse_error(self):
        """TODO:doc method
        Return:
            2000: Can not authenticate client: invalid developer key
        """
        err_code = None
        err_message = None
        for node_structs_members in self.find_structs_members():
            for node_member in node_structs_members:
                node_name, node_value = self.find_member_info(node_member)
                if node_name.text == 'code':
                    err_code = int(
                        self.find_node(tag='int', parent=node_value).text)
                if node_name.text == 'message':
                    err_message = self.find_node(
                        tag='string', parent=node_value).text
        if err_code == 2000:
            raise Exception(err_message)

    def parse_member(self, node_member):
        """
        Usage:
            self.parse_member(self.find_structs_members()[0])
        Args:
            node_member: first search members tags
        """
        members_data = list()
        print('Parsing members...')
        node_name, node_value = self.find_member_info(node_member)
        # NAME: just extract text
        name = str(node_name.text)
        # VALUE: Validations for all types
        value = None
        val_int = self.find_node('int', parent=node_value)
        val_string = self.find_node('string', parent=node_value)
        if val_int is not None and int(val_int.text) >= 0:
            value = int(val_int.text)
        if val_string is not None and len(str(val_string.text)) >= 0:
            value = str(val_string.text)
        if val_string is not None and len(str(val_string.text)) == 1:
            value = bool(val_string.text)
        # return name+value
        msg_print = "Parsing member nodes values: node_name_value={}, node_value_value={}"
        print(msg_print.format(name, value))
        members_data.append({"name": name, "value": value})
        return members_data
