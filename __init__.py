# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from work_center import ProductionWorkCenter, ProductionWorkCenterType


def register():
    Pool.register(
        ProductionWorkCenterType,
        ProductionWorkCenter,
        module='production_workcenter', type_='model'
    )
