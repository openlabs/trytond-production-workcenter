# -*- coding: utf-8 -*-
"""
    tests/test_work_center.py

    :copyright: (C) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import POOL, USER, DB_NAME, CONTEXT
from trytond.transaction import Transaction


class TestProductionWorkCenter(unittest.TestCase):
    'Test Work Center'

    def setUp(self):
        trytond.tests.test_tryton.install_module('production_workcenter')

        self.ProductionWorkCenter = POOL.get('production.work_center')
        self.ProductionWorkCenterType = POOL.get('production.work_center.type')

    def test_0010_production_work_center(self):
        'Test Production Work Center'

        with Transaction().start(DB_NAME, USER, context=CONTEXT):

            work_center_type, = self.ProductionWorkCenterType.create([{
                'name': 'Test Type',
            }])
            work_center, = self.ProductionWorkCenter.create([{
                'name': 'Test Work Center',
                'work_center_type': work_center_type.id,
            }])
            self.assertEqual(len(self.ProductionWorkCenter.search([])), 1)
