# -*- coding: utf-8 -*-
"""TODO: doc module"""


class ModelBase(object):
    """TODO: doc class"""

    def __init__(self):
        """TODO: doc method"""
        pass


class TProject(ModelBase):
    """TODO: doc class"""

    _res_members = None

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
    opt = None #noqa

    def __init__(self, res_members):
        """TODO: doc method"""
        super(TProject, self).__init__()
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
            if name == 'notes':
                self.notes = value
            if name == 'color':
                self.color = value
            if name == 'active':
                self.active = value
            if name == 'option_reqs':
                self.option_reqs = value
            if name == 'option_priority':
                self.option_priority = value
            if name == 'option_automation':
                self.option_automation = value
            if name == 'options':
                self.options = value
            if name == 'prefix':
                self.prefix = value
            if name == 'tc_counter':
                self.tc_counter = value
            if name == 'issue_tracker_enabled':
                self.issue_tracker_enabled = value
            if name == 'reqmgr_integration_enabled':
                self.reqmgr_integration_enabled = value
            if name == 'api_key':
                self.api_key = value
            # not sure if is obtaining this member struct
            if name == 'opt':
                self.opt = value


    def __repr__(self):
        return "TProject: id={}, name={}, is_public={}".format(
            self.id,
            self.name,
            self.is_public
        )



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
        return "TProject: id={}, name={}, is_public={}".format(
            self.id,
            self.name,
            self.is_public
        )

