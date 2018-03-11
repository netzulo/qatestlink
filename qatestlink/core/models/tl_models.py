# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
"""TODO: doc module"""


import re


class ModelBase(object):
    """TODO: doc class"""

    def __init__(self):
        """TODO: doc method"""
        pass

    def convert_name(self, name):
        first_cap_re = re.compile('(.)([A-Z][a-z]+)')
        all_cap_re = re.compile('([a-z0-9])([A-Z])')
        s1 = first_cap_re.sub(r'\1_\2', name)
        return all_cap_re.sub(r'\1_\2', s1).lower()


class TProject(ModelBase):
    """TODO: doc class"""

    _properties = None

    # Testlink object properties
    id = None
    name = None
    is_public = None
    notes = None
    color = None
    active = None
    option_reqs = None
    option_priority = None
    option_automation = None
    options = None
    prefix = None
    tc_counter = None
    issue_tracker_enabled = None
    reqmgr_integration_enabled = None
    api_key = None
    opt = None # noqa

    def __init__(self, properties):
        """TODO: doc method"""
        super(TProject, self).__init__()
        if properties is None:
            raise Exception('Bad param, res_member can\'t be None')
        if len(properties) <= 0:
            raise Exception(
                'Bad param, res_member can\'t be empty list')
        self._properties = properties
        self._load()

    def _load(self):
        for res_property in self._properties:
            name = self.convert_name(res_property['name'])
            value = res_property['value']
            properties_int = ['id', 'tc_counter']
            properties_bool = [
                'is_public',
                'active',
                'option_reqs',
                'option_priority',
                'option_automation',
                'issue_tracker_enabled',
                'reqmgr_integration_enabled'
            ]
            if name in properties_int:
                setattr(self, name, int(value['string']))
            elif name in properties_bool:
                setattr(self, name, bool(value['string']))
            elif name == 'opt':
                # TODO: parse this
                pass
            else:
                setattr(self, name, value['string'])

    def __repr__(self):
        return "TProject: id={}, name={}, is_public={}".format(
            self.id,
            self.name,
            self.is_public)


class TPlan(ModelBase):
    """TODO: doc class"""

    _res_members = None

    # Testlink object properties
    id = None
    name = None
    is_public = None
    active = None
    tproject_id = None
    notes = None


    def __init__(self, res_members):
        """TODO: doc method"""
        super(TPlan, self).__init__()
        if res_members is None:
            raise Exception('Bad param, res_member can\'t be None')
        if len(res_members) <= 0:
            raise Exception(
                'Bad param, res_member can\'t be empty list')
        self._res_members = res_members
        self._load()

    def _load(self):
        for res_member in self._res_members:
            name = res_member.name
            value = res_member.value
            if name == 'id':
                self.id = value
            if name == 'name':
                self.name = value
            if name == 'is_public':
                self.is_public = value
            if name == 'active':
                self.active = value
            if name == 'testproject_id':
                self.tproject_id = value
            if name == 'notes':
                self.notes = value

    def __repr__(self):
        return "TPlan: id={}, name={}, is_public={}".format(
            self.id,
            self.name,
            self.is_public)


class TSuite(ModelBase):
    """TODO: doc class"""

    _res_members = None

    # Testlink object properties
    id = None
    name = None
    parent_id = None
    node_type_id = None
    node_order = None
    node_table = None


    def __init__(self, res_members):
        """TODO: doc method"""
        super(TSuite, self).__init__()
        if res_members is None:
            raise Exception('Bad param, res_member can\'t be None')
        if len(res_members) <= 0:
            raise Exception(
                'Bad param, res_member can\'t be empty list')
        self._res_members = res_members
        self._load()

    def _load(self):
        for res_member in self._res_members:
            name = res_member.name
            value = res_member.value
            if name == 'id':
                self.id = value
            if name == 'name':
                self.name = value
            if name == 'parent_id':
                self.parent_id = value
            if name == 'node_type_id':
                self.node_type_id = value
            if name == 'node_order':
                self.node_order = value
            if name == 'node_table':
                self.node_table = value

    def __repr__(self):
        return "TSuite: id={}, name={}, parent_id={}".format(
            self.id,
            self.name,
            self.parent_id)


class TPlatform(ModelBase):
    """TODO: doc class"""

    _res_members = None

    # Testlink object properties
    id = None
    name = None
    notes = None


    def __init__(self, res_members):
        """TODO: doc method"""
        super(TPlatform, self).__init__()
        if res_members is None:
            raise Exception('Bad param, res_member can\'t be None')
        if len(res_members) <= 0:
            raise Exception(
                'Bad param, res_member can\'t be empty list')
        self._res_members = res_members
        self._load()

    def _load(self):
        for res_member in self._res_members:
            name = res_member.name
            value = res_member.value
            if name == 'id':
                self.id = value
            if name == 'name':
                self.name = value
            if name == 'notes':
                self.notes = value

    def __repr__(self):
        return "TPlatform: id={}, name={}, notes={}".format(
            self.id,
            self.name,
            self.notes)


class TBuild(ModelBase):
    """TODO: doc class"""

    _res_members = None

    # Testlink object properties
    id = None
    name = None
    notes = None
    testplan_id = None
    active = None
    is_open = None
    release_date = None
    closed_on_date = None
    creation_ts = None


    def __init__(self, res_members):
        """TODO: doc method"""
        super(TBuild, self).__init__()
        if res_members is None:
            raise Exception('Bad param, res_member can\'t be None')
        if len(res_members) <= 0:
            raise Exception(
                'Bad param, res_member can\'t be empty list')
        self._res_members = res_members
        self._load()

    def _load(self):
        for res_member in self._res_members:
            name = res_member.name
            value = res_member.value
            if name == 'id':
                self.id = value
            if name == 'name':
                self.name = value
            if name == 'notes':
                self.notes = value
            if name == 'testplan_id':
                self.testplan_id = value
            if name == 'active':
                self.active = value
            if name == 'is_open':
                self.is_open = value
            if name == 'release_date':
                self.release_date = value
            if name == 'closed_on_date':
                self.closed_on_date = value
            if name == 'creation_ts':
                self.creation_ts = value

    def __repr__(self):
        return "TBuild: id={}, name={}, notes={}, testplan_id={}".format(
            self.id,
            self.name,
            self.notes,
            self.testplan_id)


class TCase(ModelBase):
    """TODO: doc class"""

    _res_members = None

    # Testlink object properties
    id = None
    name = None
    notes = None


    def __init__(self, res_members):
        """TODO: doc method"""
        super(TCase, self).__init__()
        if res_members is None:
            raise Exception('Bad param, res_member can\'t be None')
        if len(res_members) <= 0:
            raise Exception(
                'Bad param, res_member can\'t be empty list')
        self._res_members = res_members
        self._load()

    def _load(self):
        for res_member in self._res_members:
            name = res_member.name
            value = res_member.value
            if name == 'id':
                self.id = value
            if name == 'name':
                self.name = value
            if name == 'notes':
                self.notes = value

    def __repr__(self):
        return "TCase: id={}, name={}, notes={}".format(
            self.id,
            self.name,
            self.notes)