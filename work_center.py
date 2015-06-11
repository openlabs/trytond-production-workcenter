# -*- coding: utf-8 -*-
"""
    production.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import ModelSQL, ModelView, fields
from trytond.pyson import Eval

__all__ = ['ProductionWorkCenter', 'ProductionWorkCenterType']

STATES = {
    'readonly': ~Eval('active', True),
}
DEPENDS = ['active']


class ProductionWorkCenterType(ModelSQL, ModelView):
    "Work Center Type"
    __name__ = 'production.work_center.type'

    active = fields.Boolean('Active', select=True)
    name = fields.Char(
        'Name', required=True, select=True, states=STATES, depends=DEPENDS
    )
    work_centeres = fields.One2Many(
        'production.work_center', 'work_center_type', 'Work Centeres'
    )

    @staticmethod
    def default_active():
        return True


class ProductionWorkCenter(ModelSQL, ModelView):
    "Work Center"
    __name__ = 'production.work_center'

    active = fields.Boolean('Active', select=True)
    name = fields.Char(
        'Name', required=True, select=True, states=STATES, depends=DEPENDS
    )
    work_center_type = fields.Many2One(
        'production.work_center.type', 'Type', select=True,
        required=True, states=STATES, depends=DEPENDS)

    @staticmethod
    def default_active():
        return True
