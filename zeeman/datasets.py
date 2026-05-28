#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:26:48 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/git_repo/zeeman/datasets.py, 2026-05-28 Thursday 18:28:49 nclotta>

import importlib.util as ilu
import pathlib
import sys

d = pathlib.Path("./zeedat")

def load_ext(fp):
    spec = ilu.spec_from_file_location(fp.stem, fp)
    if spec and spec.loader:
        md = ilu.module_from_spec(spec)
        sys.modules[fp.stem] = md
        spec.loader.exec_module(md)
        return md
    else:
        return None

all = []
__internal__data_text = set()

for q in d.glob("*/"):
    if q.is_dir():
        for p in q.glob("data*.py"):
            all.append([load_ext(p), q.stem, p.stem])
            __internal__data_text.add(q.stem)

select = {ds: [] for ds in __internal__data_text}
for q in all:
    select[q[1]].append(q)

# eof
