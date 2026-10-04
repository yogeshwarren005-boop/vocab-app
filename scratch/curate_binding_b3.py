# -*- coding: utf-8 -*-
"""
Assembles all 106 words across Cluster Binding:
- Dashboard — lig (66 words): part1_lig (33) + part2_lig (33)
- Dashboard — strict (23 words): part3_strict (23)
- Dashboard — string (17 words): part4_string (17)
Total: 66 + 23 + 17 = 106 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.part1_lig import part1_lig
from scratch.part2_lig import part2_lig
from scratch.part3_strict import part3_strict
from scratch.part4_string import part4_string

data_binding_b3 = {}
data_binding_b3.update(part1_lig)
data_binding_b3.update(part2_lig)
data_binding_b3.update(part3_strict)
data_binding_b3.update(part4_string)

if __name__ == "__main__":
    print(f"Total entries in data_binding_b3: {len(data_binding_b3)}")
