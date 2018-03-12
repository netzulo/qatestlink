# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
"""TODO: doc module"""


import re


class ModelBase(object):
    """TODO: doc class"""

    # Testlink common object properties
    id = None
    name = None

    def __init__(self, properties, properties_int=None, properties_bool=None):
        """TODO: doc method"""
        if properties is None:
            raise Exception('Bad param, res_member can\'t be None')
        if len(properties) <= 0:
            raise Exception(
                'Bad param, res_member can\'t be empty list')
        self._properties = properties
        if not properties_int:
            properties_int = []
        self._properties_int = properties_int
        if not properties_bool:
            properties_bool = []
        self._properties_bool = properties_bool
        self._load()

    def _load(self):
        for res_property in self._properties:
            name = self.convert_name(res_property['name'])
            value = res_property['value']
            if name in self._properties_int:
                setattr(self, name, int(value['string']))
            elif name in self._properties_bool:
                setattr(self, name, bool(value['string']))
            else:
                if value.get('string', None):
                    setattr(self, name, value['string'])
                if value.get('struct', None):
                    setattr(self, name, 'NOT_IMPLEMENTED')

    def convert_name(self, name):
        first_cap_re = re.compile('(.)([A-Z][a-z]+)')
        all_cap_re = re.compile('([a-z0-9])([A-Z])')
        s1 = first_cap_re.sub(r'\1_\2', name)
        return all_cap_re.sub(r'\1_\2', s1).lower()


class TProject(ModelBase):
    """TODO: doc class"""

    # Testlink object properties
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

    def __init__(self, properties, properties_int=None, properties_bool=None):
        """TODO: doc method"""
        super(TProject, self).__init__(
            properties,
            properties_int=['id', 'tc_counter'],
            properties_bool=[
                'is_public',
                'active',
                'option_reqs',
                'option_priority',
                'option_automation',
                'issue_tracker_enabled',
                'reqmgr_integration_enabled'
            ]
        )

    def __repr__(self):
        return "TProject: id={}, name={}, is_public={}".format(
            self.id,
            self.name,
            self.is_public)


class TPlan(ModelBase):
    """TODO: doc class"""

    # Testlink object properties
    is_public = None
    active = None
    tproject_id = None
    notes = None

    def __init__(self, properties):
        """TODO: doc method"""
        super(TPlan, self).__init__(
            properties,
            properties_int=['id', 'testproject_id'],
            properties_bool=['is_public', 'active']
        )

    def __repr__(self):
        return "TPlan: id={}, name={}, is_public={}".format(
            self.id,
            self.name,
            self.is_public)


class TSuite(ModelBase):
    """TODO: doc class"""

    # Testlink object properties
    parent_id = None
    node_type_id = None
    node_order = None
    node_table = None
    is_public = None
    active = None

    def __init__(self, properties):
        """TODO: doc method"""
        super(TSuite, self).__init__(
            properties,
            properties_int=[
                'id',
                'parent_id',
                'node_type_id',
                'node_order'
            ],
            properties_bool=['is_public', 'active']
        )

    def __repr__(self):
        return "TSuite: id={}, name={}, parent_id={}".format(
            self.id,
            self.name,
            self.parent_id)


class TPlatform(ModelBase):
    """TODO: doc class"""

    # Testlink object properties
    notes = None

    def __init__(self, properties):
        """TODO: doc method"""
        super(TPlatform, self).__init__(
            properties,
            properties_int=['id'],
            properties_bool=[]
        )

    def __repr__(self):
        return "TPlatform: id={}, name={}, notes={}".format(
            self.id,
            self.name,
            self.notes)


class TBuild(ModelBase):
    """TODO: doc class"""

    # Testlink object properties
    notes = None
    testplan_id = None
    active = None
    is_open = None
    release_date = None
    closed_on_date = None
    creation_ts = None

    def __init__(self, properties):
        """TODO: doc method"""
        super(TBuild, self).__init__(
            properties,
            properties_int=['id', 'testplan_id'],
            properties_bool=['active', 'is_open']
        )

    def __repr__(self):
        return "TBuild: id={}, name={}, notes={}, testplan_id={}".format(
            self.id,
            self.name,
            self.notes,
            self.testplan_id)


class TCase(ModelBase):
    """TODO: doc class"""

    # Testlink object properties
    notes = None

    def __init__(self, properties):
        """TODO: doc method"""
        super(TCase, self).__init__(
            properties,
            properties_int=['id', 'tcase_id'],
            properties_bool=None
        )

    def _load(self):
        super(TCase, self)._load()
        for res_property in self._properties:
            name = self.convert_name(res_property['name'])
            value = res_property['value']
            if name == 'tcase_id':
                setattr(self, 'id', int(value['string']))
            if name == 'tcase_name':
                setattr(self, 'name', value['string'])

    def __repr__(self):
        return "TCase: id={}, name={}, notes={}".format(
            self.id,
            self.name,
            self.notes)
