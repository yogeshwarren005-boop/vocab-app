# -*- coding: utf-8 -*-
"""
Assembles all 92 words across Dashboard — opt, Dashboard — rob, Dashboard — virt:
- opt (39 words): part1_opt (25) + part2_opt (14)
- rob (43 words): part1_rob (22) + part2_rob (21)
- virt (10 words): part1_virt (10)
Total: 39 + 43 + 10 = 92 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.part1_opt import part1_opt
from scratch.part2_opt import part2_opt
from scratch.part1_rob import part1_rob
from scratch.part2_rob import part2_rob
from scratch.part1_virt import part1_virt

data_virtue_opt_rob_virt = {}
data_virtue_opt_rob_virt.update(part1_opt)
data_virtue_opt_rob_virt.update(part2_opt)
data_virtue_opt_rob_virt.update(part1_rob)
data_virtue_opt_rob_virt.update(part2_rob)
data_virtue_opt_rob_virt.update(part1_virt)

if __name__ == "__main__":
    print(f"Total entries in data_virtue_opt_rob_virt: {len(data_virtue_opt_rob_virt)}")
