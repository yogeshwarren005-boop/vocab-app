# -*- coding: utf-8 -*-
"""
Full dataset for Cluster Binding: Dashboard — ser (117 words)
Assembles parts 1, 2, 3, and 4 into a single dictionary data_binding_ser.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_ser_part1 import data_part1
from scratch.curate_ser_part2 import data_part2
from scratch.curate_ser_part3 import data_part3
from scratch.curate_ser_part4 import data_part4

data_binding_ser = {}
data_binding_ser.update(data_part1)
data_binding_ser.update(data_part2)
data_binding_ser.update(data_part3)
data_binding_ser.update(data_part4)
