# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestOperator::test_simple_expr 1'] = '''float fn(float a, float b){
  return a*b + a
}'''

snapshots['TestOperator::test_simple_str 1'] = '''float fn(float a, float b){
  return a*b
}'''
